import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import yaml


SCHEMA_URL = "https://opendataproducts.org/odpg-v1.0/schema/graph.yaml"
DEFAULT_NODE_TYPE = "Resource"
DEFAULT_EDGE_TYPE = "relatedTo"
DEFAULT_CONFIDENCE = "medium"


FORMAT_ALIASES = {
    "cypher": "opencypher",
    "open-cypher": "opencypher",
    "open_cypher": "opencypher",
    "sparql": "rdf",
    "geosparql": "rdf",
    "ttl": "rdf",
    "turtle": "rdf",
    "nt": "rdf",
    "ntriples": "rdf",
    "n-triples": "rdf",
}


def convert_graph(
    source: Any,
    source_format: str,
    graph_id: str | None = None,
    name: str | None = None,
    description: str | None = None,
    confidence: str = DEFAULT_CONFIDENCE,
) -> dict[str, Any]:
    normalized = normalize_format(source_format)
    builder = ODPGBuilder(graph_id=graph_id, name=name, description=description, confidence=confidence)

    if normalized == "jsonld":
        convert_jsonld(source, builder)
    elif normalized == "graphml":
        convert_graphml(str(source), builder)
    elif normalized == "graphson":
        convert_graphson(source, builder)
    elif normalized == "rdf":
        convert_rdf(str(source), builder)
    elif normalized in {"opencypher", "gql"}:
        convert_property_graph_script(str(source), builder)
    elif normalized == "gremlin":
        convert_gremlin(str(source), builder)
    else:
        raise ValueError(f"Unsupported graph format: {source_format}")

    return builder.document()


def run_convert(
    input_path: Path,
    output_path: Path | None = None,
    source_format: str | None = None,
    graph_id: str | None = None,
    name: str | None = None,
    description: str | None = None,
    confidence: str = DEFAULT_CONFIDENCE,
) -> int:
    if not input_path.is_file():
        raise FileNotFoundError(f"Graph file not found: {input_path}")

    resolved_format = normalize_format(source_format or infer_format(input_path))
    source = read_source(input_path, resolved_format)
    if resolved_format == "json":
        resolved_format = infer_json_format(source)
    document = convert_graph(
        source,
        source_format=resolved_format,
        graph_id=graph_id or input_path.stem,
        name=name,
        description=description,
        confidence=confidence,
    )
    yaml_text = yaml.safe_dump(document, sort_keys=False, allow_unicode=True)
    if output_path:
        output_path.write_text(yaml_text, encoding="utf-8")
    else:
        print(yaml_text, end="")
    return 0


def command_convert(args: argparse.Namespace) -> int:
    return run_convert(
        args.input,
        args.output,
        source_format=args.format,
        graph_id=args.id,
        name=args.name,
        description=args.description,
        confidence=args.confidence,
    )


class ODPGBuilder:
    def __init__(
        self,
        graph_id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        confidence: str = DEFAULT_CONFIDENCE,
    ) -> None:
        self.graph_id = graph_id or "converted-graph"
        self.name = name or "Converted Graph"
        self.description = description or "Graph converted to ODPG from an external graph format."
        self.confidence = confidence or DEFAULT_CONFIDENCE
        self.nodes_by_id: dict[str, dict[str, str]] = {}
        self.edges: list[dict[str, str]] = []
        self.edge_keys: set[tuple[str, str, str]] = set()

    def add_node(self, node_id: Any, node_type: Any = None, ref: Any = None) -> str:
        normalized_id = clean_identifier(node_id)
        if not normalized_id:
            raise ValueError("Cannot add an ODPG node without an id")
        normalized_type = local_name(clean_identifier(node_type)) or DEFAULT_NODE_TYPE
        node_ref = clean_identifier(ref) or f"#{normalized_id}"

        existing = self.nodes_by_id.get(normalized_id)
        if existing:
            if existing["type"] == DEFAULT_NODE_TYPE and normalized_type != DEFAULT_NODE_TYPE:
                existing["type"] = normalized_type
            if existing["$ref"].startswith("#") and node_ref and not node_ref.startswith("#"):
                existing["$ref"] = node_ref
            return normalized_id

        self.nodes_by_id[normalized_id] = {"id": normalized_id, "type": normalized_type, "$ref": node_ref}
        return normalized_id

    def add_edge(
        self,
        source: Any,
        target: Any,
        edge_type: Any = None,
        confidence: str | None = None,
    ) -> None:
        source_id = self.add_node(source)
        target_id = self.add_node(target)
        normalized_type = local_name(clean_identifier(edge_type)) or DEFAULT_EDGE_TYPE
        key = (source_id, target_id, normalized_type)
        if key in self.edge_keys:
            return
        self.edge_keys.add(key)
        self.edges.append(
            {
                "from": source_id,
                "to": target_id,
                "type": normalized_type,
                "confidence": confidence or self.confidence,
            }
        )

    def document(self) -> dict[str, Any]:
        return {
            "schema": SCHEMA_URL,
            "version": 1.0,
            "kind": "Graph",
            "graph": {
                "metadata": {
                    "id": self.graph_id,
                    "name": {"en": self.name},
                    "description": {"en": self.description},
                },
                "nodes": list(self.nodes_by_id.values()),
                "edges": self.edges,
            },
        }


def normalize_format(source_format: str) -> str:
    normalized = source_format.strip().lower()
    return FORMAT_ALIASES.get(normalized, normalized)


def infer_format(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".jsonld":
        return "jsonld"
    if suffix == ".graphml":
        return "graphml"
    if suffix == ".graphson":
        return "graphson"
    if suffix in {".rdf", ".ttl", ".nt", ".n3"}:
        return "rdf"
    if suffix in {".cypher", ".cql"}:
        return "opencypher"
    if suffix == ".gql":
        return "gql"
    if suffix in {".gremlin", ".groovy"}:
        return "gremlin"
    if suffix == ".json":
        return "json"
    raise ValueError(f"Could not infer graph format from file extension: {path.suffix}")


def read_source(path: Path, source_format: str) -> Any:
    text = path.read_text(encoding="utf-8-sig")
    if source_format == "json":
        return json.loads(text)
    if source_format in {"jsonld", "graphson"}:
        return json.loads(text)
    return text


def infer_json_format(data: Any) -> str:
    if isinstance(data, dict) and ("@graph" in data or "@context" in data or "@id" in data):
        return "jsonld"
    if isinstance(data, dict) and ("vertices" in data or "nodes" in data or "edges" in data):
        return "graphson"
    if isinstance(data, list):
        return "jsonld"
    raise ValueError("JSON input must look like JSON-LD or GraphSON, or pass --format explicitly")


def convert_jsonld(source: Any, builder: ODPGBuilder) -> None:
    objects = jsonld_objects(source)
    known_ids = {
        clean_identifier(item.get("@id"))
        for item in objects
        if isinstance(item, dict) and clean_identifier(item.get("@id"))
    }

    for item in objects:
        if not isinstance(item, dict):
            continue
        node_id = clean_identifier(item.get("@id"))
        if not node_id:
            continue
        builder.add_node(node_id, jsonld_type(item.get("@type")))

    for item in objects:
        if not isinstance(item, dict):
            continue
        source_id = clean_identifier(item.get("@id"))
        if not source_id:
            continue
        for predicate, value in item.items():
            if predicate.startswith("@"):
                continue
            for target in jsonld_references(value):
                if target in known_ids:
                    builder.add_edge(source_id, target, predicate)


def jsonld_objects(source: Any) -> list[dict[str, Any]]:
    if isinstance(source, list):
        return [item for item in source if isinstance(item, dict)]
    if not isinstance(source, dict):
        raise ValueError("JSON-LD source must be a JSON object or array")
    graph = source.get("@graph")
    if isinstance(graph, list):
        return [item for item in graph if isinstance(item, dict)]
    if source.get("@id"):
        return [source]
    return []


def jsonld_type(value: Any) -> str:
    if isinstance(value, list):
        return local_name(clean_identifier(value[0])) if value else DEFAULT_NODE_TYPE
    return local_name(clean_identifier(value)) or DEFAULT_NODE_TYPE


def jsonld_references(value: Any) -> list[str]:
    if isinstance(value, dict):
        target = clean_identifier(value.get("@id"))
        return [target] if target else []
    if isinstance(value, list):
        references: list[str] = []
        for item in value:
            references.extend(jsonld_references(item))
        return references
    return []


def convert_graphml(source: str, builder: ODPGBuilder) -> None:
    root = ET.fromstring(source)
    keys: dict[str, str] = {}
    for key in root.findall(".//{*}key"):
        key_id = clean_identifier(key.attrib.get("id"))
        attr_name = clean_identifier(key.attrib.get("attr.name"))
        if key_id and attr_name:
            keys[key_id] = attr_name

    for node in root.findall(".//{*}node"):
        node_id = clean_identifier(node.attrib.get("id"))
        if not node_id:
            continue
        data = graphml_data(node, keys)
        builder.add_node(node_id, data.get("type") or data.get("label") or DEFAULT_NODE_TYPE)

    for edge in root.findall(".//{*}edge"):
        source_id = clean_identifier(edge.attrib.get("source"))
        target_id = clean_identifier(edge.attrib.get("target"))
        if not source_id or not target_id:
            continue
        data = graphml_data(edge, keys)
        builder.add_edge(source_id, target_id, data.get("type") or data.get("label") or DEFAULT_EDGE_TYPE)


def graphml_data(element: ET.Element, keys: dict[str, str]) -> dict[str, str]:
    data: dict[str, str] = {}
    for child in element.findall("{*}data"):
        key = clean_identifier(child.attrib.get("key"))
        name = keys.get(key, key)
        if name:
            data[name] = clean_identifier(child.text)
    return data


def convert_graphson(source: Any, builder: ODPGBuilder) -> None:
    data = unwrap_graphson(source)
    if not isinstance(data, dict):
        raise ValueError("GraphSON source must be a JSON object")

    vertices = data.get("vertices") or data.get("nodes") or data.get("V") or []
    edges = data.get("edges") or data.get("E") or []

    if isinstance(vertices, dict):
        vertices = list(vertices.values())
    if isinstance(edges, dict):
        edges = list(edges.values())

    for vertex in vertices:
        if not isinstance(vertex, dict):
            continue
        node_id = vertex.get("id") or vertex.get("_id")
        label = vertex.get("label") or vertex.get("type") or vertex.get("_label")
        if node_id is not None:
            builder.add_node(node_id, label)

    for edge in edges:
        if not isinstance(edge, dict):
            continue
        source_id = edge.get("outV") or edge.get("source") or edge.get("from") or edge.get("_outV")
        target_id = edge.get("inV") or edge.get("target") or edge.get("to") or edge.get("_inV")
        label = edge.get("label") or edge.get("type") or edge.get("_label")
        if source_id is not None and target_id is not None:
            builder.add_edge(source_id, target_id, label)


def unwrap_graphson(value: Any) -> Any:
    if isinstance(value, dict):
        if "@value" in value and set(value.keys()).issubset({"@type", "@value"}):
            return unwrap_graphson(value["@value"])
        return {key: unwrap_graphson(item) for key, item in value.items()}
    if isinstance(value, list):
        return [unwrap_graphson(item) for item in value]
    return value


TRIPLE_RE = re.compile(
    r"^\s*(?P<s><[^>]+>|_:[A-Za-z0-9_-]+|[A-Za-z][\w.-]*:[^\s]+)\s+"
    r"(?P<p>a|<[^>]+>|[A-Za-z][\w.-]*:[^\s]+)\s+"
    r"(?P<o><[^>]+>|_:[A-Za-z0-9_-]+|[A-Za-z][\w.-]*:[^\s]+|\"(?:\\.|[^\"])*\"(?:@\w+|\^\^<[^>]+>)?)\s*\.\s*$"
)


def convert_rdf(source: str, builder: ODPGBuilder) -> None:
    typed_nodes: dict[str, str] = {}
    edges: list[tuple[str, str, str]] = []
    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("@prefix") or line.upper().startswith("PREFIX"):
            continue
        match = TRIPLE_RE.match(line)
        if not match:
            continue
        subject = clean_rdf_term(match.group("s"))
        predicate = clean_rdf_term(match.group("p"))
        rdf_object = match.group("o")
        if rdf_object.startswith('"'):
            continue
        target = clean_rdf_term(rdf_object)
        if predicate in {"a", "rdf:type"} or local_name(predicate) == "type":
            typed_nodes[subject] = local_name(target) or DEFAULT_NODE_TYPE
        else:
            edges.append((subject, target, predicate))

    for node_id, node_type in typed_nodes.items():
        builder.add_node(node_id, node_type)
    for source_id, target_id, edge_type in edges:
        builder.add_edge(source_id, target_id, edge_type)


NODE_PATTERN = re.compile(
    r"\((?P<var>[A-Za-z_]\w*)?\s*(?::(?P<label>[A-Za-z_][\w.-]*))?\s*(?:\{(?P<props>[^}]*)\})?\)"
)
EDGE_PATTERN = re.compile(
    r"\((?P<left>[A-Za-z_]\w*)[^\)]*\)\s*-\s*\[\s*(?::(?P<label>[A-Za-z_][\w.-]*))?[^\]]*\]\s*->\s*\((?P<right>[A-Za-z_]\w*)[^\)]*\)"
)
PROP_PATTERN = re.compile(r"(?P<key>[A-Za-z_]\w*)\s*:\s*['\"](?P<value>[^'\"]+)['\"]")


def convert_property_graph_script(source: str, builder: ODPGBuilder) -> None:
    variables: dict[str, str] = {}

    for match in NODE_PATTERN.finditer(source):
        variable = clean_identifier(match.group("var"))
        label = clean_identifier(match.group("label"))
        props = parse_properties(match.group("props") or "")
        if not label and not props:
            continue
        node_id = props.get("id") or props.get("name") or variable
        if node_id:
            builder.add_node(node_id, label or DEFAULT_NODE_TYPE)
            if variable:
                variables[variable] = node_id

    for match in EDGE_PATTERN.finditer(source):
        source_id = variables.get(match.group("left"), match.group("left"))
        target_id = variables.get(match.group("right"), match.group("right"))
        builder.add_edge(source_id, target_id, match.group("label") or DEFAULT_EDGE_TYPE)


def parse_properties(source: str) -> dict[str, str]:
    return {match.group("key"): match.group("value") for match in PROP_PATTERN.finditer(source)}


ADD_VERTEX_RE = re.compile(
    r"addV\(['\"](?P<label>[^'\"]+)['\"]\)(?P<props>(?:\.property\(['\"][^'\"]+['\"],\s*['\"][^'\"]+['\"]\))*)"
)
GREMLIN_PROP_RE = re.compile(r"\.property\(['\"](?P<key>[^'\"]+)['\"],\s*['\"](?P<value>[^'\"]+)['\"]\)")
ADD_EDGE_RE = re.compile(
    r"(?P<out>[A-Za-z_][\w.-]*)\.addEdge\(['\"](?P<label>[^'\"]+)['\"],\s*(?P<in>[A-Za-z_][\w.-]*)\)"
)


def convert_gremlin(source: str, builder: ODPGBuilder) -> None:
    for match in ADD_VERTEX_RE.finditer(source):
        props = {prop.group("key"): prop.group("value") for prop in GREMLIN_PROP_RE.finditer(match.group("props"))}
        node_id = props.get("id") or props.get("name") or f"{match.group('label')}-{len(builder.nodes_by_id) + 1}"
        builder.add_node(node_id, match.group("label"))

    for match in ADD_EDGE_RE.finditer(source):
        builder.add_edge(match.group("out"), match.group("in"), match.group("label"))


def clean_identifier(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def clean_rdf_term(value: str) -> str:
    cleaned = value.strip()
    if cleaned.startswith("<") and cleaned.endswith(">"):
        return cleaned[1:-1]
    return cleaned


def local_name(value: str) -> str:
    cleaned = clean_rdf_term(value)
    if not cleaned:
        return ""
    for separator in ("#", "/", ":"):
        if separator in cleaned:
            cleaned = cleaned.rsplit(separator, 1)[-1]
    return cleaned


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert common graph formats to ODPG YAML.")
    parser.add_argument("-i", "--input", required=True, type=Path, help="Path to source graph file")
    parser.add_argument("-o", "--output", type=Path, help="Path to write ODPG YAML")
    parser.add_argument(
        "--format",
        choices=["jsonld", "rdf", "graphml", "opencypher", "gql", "gremlin", "graphson", "geosparql"],
        help="Source graph format. Inferred from extension when omitted.",
    )
    parser.add_argument("--id", help="ODPG graph metadata id")
    parser.add_argument("--name", help="ODPG graph metadata name")
    parser.add_argument("--description", help="ODPG graph metadata description")
    parser.add_argument(
        "--confidence",
        choices=["high", "medium", "low"],
        default=DEFAULT_CONFIDENCE,
        help="Confidence value assigned to converted edges",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return command_convert(args)


if __name__ == "__main__":
    raise SystemExit(main())
