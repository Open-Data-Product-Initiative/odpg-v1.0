import argparse
import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIDENCE_VALUES = {"high", "medium", "low"}
CORE_NODE_TYPES = {
    "DataProduct",
    "UseCase",
    "BusinessObjective",
    "KPI",
    "Domain",
    "Dataset",
    "API",
    "Policy",
    "Workflow",
    "Agent",
    "Capability",
    "StrategicOpportunity",
}
CORE_EDGE_TYPES = {
    "uses",
    "supports",
    "contributesTo",
    "measures",
    "tracks",
    "dependsOn",
    "produces",
    "consumes",
    "governedBy",
    "ownedBy",
    "alignsWith",
    "alignWith",
    "relatedTo",
    "impacts",
    "derivedFrom",
    "exposes",
    "monitors",
    "identifies",
}


def load_graph(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Graph file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Graph file must contain a YAML object")
    return data


def graph_payload(document: dict[str, Any]) -> dict[str, Any]:
    payload = document.get("graph")
    return payload if isinstance(payload, dict) else document


def graph_metadata(document: dict[str, Any]) -> dict[str, Any]:
    payload = graph_payload(document)
    metadata = payload.get("metadata")
    return metadata if isinstance(metadata, dict) else {}


def localized_text(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("en") or next(iter(value.values()), ""))
    return "" if value is None else str(value)


def node_ref(node: dict[str, Any]) -> str:
    return str(node.get("$ref") or node.get("ref") or "")


def validate_graph(document: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for field in ("schema", "version", "kind"):
        if field not in document:
            errors.append(f"Missing required root field: {field}")

    if document.get("kind") != "Graph":
        errors.append("Invalid root field kind: expected Graph")

    payload = graph_payload(document)
    metadata = graph_metadata(document)
    nodes = payload.get("nodes")
    edges = payload.get("edges")

    if "graph" in document and not isinstance(document.get("graph"), dict):
        errors.append("Root field graph must be an object")

    if not isinstance(nodes, list):
        errors.append("Missing or invalid graph.nodes array")
        nodes = []
    if not isinstance(edges, list):
        errors.append("Missing or invalid graph.edges array")
        edges = []

    for field in ("id", "name", "description"):
        if field not in metadata:
            errors.append(f"Missing required metadata field: graph.metadata.{field}")

    node_ids: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"Node at index {index} must be an object")
            continue
        node_id = node.get("id")
        node_type = node.get("type")
        if not node_id:
            errors.append(f"Node at index {index} is missing required field: id")
        elif str(node_id) in node_ids:
            errors.append(f"Duplicate node id found: {node_id}")
        else:
            node_ids.add(str(node_id))
        if not node_type:
            errors.append(f"Node {node_id or index} is missing required field: type")
        elif str(node_type) not in CORE_NODE_TYPES:
            warnings.append(f"Node {node_id or index} uses non-core node type: {node_type}")
        if not node_ref(node):
            errors.append(f"Node {node_id or index} is missing required field: $ref")

    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"Edge at index {index} must be an object")
            continue
        source = str(edge.get("from") or "")
        target = str(edge.get("to") or "")
        edge_type = str(edge.get("type") or "")
        confidence = str(edge.get("confidence") or "")
        if not source:
            errors.append(f"Edge at index {index} is missing required field: from")
        elif source not in node_ids:
            errors.append(f"Edge source does not match any node id: {source}")
        if not target:
            errors.append(f"Edge at index {index} is missing required field: to")
        elif target not in node_ids:
            errors.append(f"Edge target does not match any node id: {target}")
        if not edge_type:
            errors.append(f"Edge {source}->{target} is missing required field: type")
        elif edge_type not in CORE_EDGE_TYPES:
            warnings.append(f"Edge {source}->{target} uses non-core edge type: {edge_type}")
        if not confidence:
            errors.append(f"Edge {source}->{target} is missing required field: confidence")
        elif confidence not in DEFAULT_CONFIDENCE_VALUES:
            errors.append(
                f"Edge {source}->{target} has invalid confidence: {confidence}. "
                "Use high, medium, or low."
            )

    return errors, warnings


def build_adjacency(document: dict[str, Any], reverse: bool = False) -> dict[str, list[dict[str, Any]]]:
    adjacency: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge in graph_payload(document).get("edges") or []:
        if not isinstance(edge, dict):
            continue
        source = str(edge.get("from") or "")
        target = str(edge.get("to") or "")
        key = target if reverse else source
        adjacency[key].append(edge)
    return adjacency


def summarize_graph(document: dict[str, Any]) -> dict[str, Any]:
    payload = graph_payload(document)
    metadata = graph_metadata(document)
    nodes = [n for n in payload.get("nodes") or [] if isinstance(n, dict)]
    edges = [e for e in payload.get("edges") or [] if isinstance(e, dict)]

    node_types: dict[str, int] = defaultdict(int)
    edge_types: dict[str, int] = defaultdict(int)
    confidence_values: dict[str, int] = defaultdict(int)

    for node in nodes:
        node_types[str(node.get("type") or "unknown")] += 1
    for edge in edges:
        edge_types[str(edge.get("type") or "unknown")] += 1
        confidence_values[str(edge.get("confidence") or "unknown")] += 1

    return {
        "id": metadata.get("id"),
        "name": localized_text(metadata.get("name")),
        "description": localized_text(metadata.get("description")),
        "nodeCount": len(nodes),
        "edgeCount": len(edges),
        "nodeTypes": dict(sorted(node_types.items())),
        "edgeTypes": dict(sorted(edge_types.items())),
        "confidenceValues": dict(sorted(confidence_values.items())),
    }


def traverse_graph(
    document: dict[str, Any],
    start: str,
    depth: int,
    relationship: str | None = None,
    reverse: bool = False,
) -> list[dict[str, Any]]:
    adjacency = build_adjacency(document, reverse=reverse)
    paths: list[dict[str, Any]] = []
    queue: deque[tuple[str, list[dict[str, Any]]]] = deque([(start, [])])
    seen: set[tuple[str, int]] = {(start, 0)}

    while queue:
        node_id, path = queue.popleft()
        if len(path) >= depth:
            continue
        for edge in adjacency.get(node_id, []):
            if relationship and edge.get("type") != relationship:
                continue
            next_node = str(edge.get("from") if reverse else edge.get("to"))
            next_path = path + [edge]
            paths.append(
                {
                    "start": start,
                    "end": next_node,
                    "depth": len(next_path),
                    "relationships": [
                        {
                            "from": item.get("from"),
                            "to": item.get("to"),
                            "type": item.get("type"),
                            "confidence": item.get("confidence"),
                        }
                        for item in next_path
                    ],
                }
            )
            state = (next_node, len(next_path))
            if state not in seen:
                seen.add(state)
                queue.append((next_node, next_path))

    return paths


def analyze_graph(document: dict[str, Any]) -> dict[str, Any]:
    payload = graph_payload(document)
    nodes = [n for n in payload.get("nodes") or [] if isinstance(n, dict)]
    edges = [e for e in payload.get("edges") or [] if isinstance(e, dict)]
    node_by_id = {str(node.get("id")): node for node in nodes if node.get("id")}

    incoming: dict[str, list[dict[str, Any]]] = defaultdict(list)
    outgoing: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge in edges:
        outgoing[str(edge.get("from") or "")].append(edge)
        incoming[str(edge.get("to") or "")].append(edge)

    orphan_kpis = [
        node_id
        for node_id, node in node_by_id.items()
        if node.get("type") == "KPI"
        and not any(edge.get("type") == "measures" for edge in outgoing.get(node_id, []))
    ]
    unsupported_objectives = [
        node_id
        for node_id, node in node_by_id.items()
        if node.get("type") == "BusinessObjective"
        and not any(edge.get("type") in {"supports", "contributesTo", "alignsWith", "alignWith"} for edge in incoming.get(node_id, []))
    ]
    ungoverned_assets = [
        node_id
        for node_id, node in node_by_id.items()
        if node.get("type") in {"DataProduct", "API", "Dataset", "Workflow", "Agent"}
        and not any(edge.get("type") == "governedBy" for edge in outgoing.get(node_id, []))
    ]
    weak_relationships = [
        {
            "from": edge.get("from"),
            "to": edge.get("to"),
            "type": edge.get("type"),
            "confidence": edge.get("confidence"),
        }
        for edge in edges
        if edge.get("confidence") == "low"
    ]
    potential_opportunities = [
        node_id
        for node_id, node in node_by_id.items()
        if node.get("type") == "UseCase"
        and any(edge.get("type") == "uses" for edge in outgoing.get(node_id, []))
        and not any(edge.get("type") in {"supports", "contributesTo"} for edge in outgoing.get(node_id, []))
    ]

    return {
        "orphanKpis": orphan_kpis,
        "unsupportedBusinessObjectives": unsupported_objectives,
        "ungovernedAssets": ungoverned_assets,
        "lowConfidenceRelationships": weak_relationships,
        "useCasesWithoutStrategicContribution": potential_opportunities,
    }


def agent_context(document: dict[str, Any], node_id: str, depth: int) -> dict[str, Any]:
    payload = graph_payload(document)
    nodes = [n for n in payload.get("nodes") or [] if isinstance(n, dict)]
    node_by_id = {str(node.get("id")): node for node in nodes if node.get("id")}
    forward_paths = traverse_graph(document, node_id, depth)
    reverse_paths = traverse_graph(document, node_id, depth, reverse=True)
    related_ids = {node_id}
    for path in forward_paths + reverse_paths:
        related_ids.add(str(path.get("end")))

    return {
        "focusNode": node_by_id.get(node_id, {"id": node_id}),
        "relatedNodes": [node_by_id[node] for node in sorted(related_ids) if node in node_by_id],
        "forwardPaths": forward_paths,
        "reversePaths": reverse_paths,
        "governanceSignals": [
            path
            for path in forward_paths
            if any(item.get("type") == "governedBy" for item in path.get("relationships", []))
        ],
    }


def write_output(data: Any, path: Path | None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if path:
        path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def command_validate(args: argparse.Namespace) -> int:
    document = load_graph(args.input)
    errors, warnings = validate_graph(document)
    result = {"valid": not errors, "errors": errors, "warnings": warnings}
    write_output(result, args.output)
    return 0 if not errors else 1


def command_summary(args: argparse.Namespace) -> int:
    write_output(summarize_graph(load_graph(args.input)), args.output)
    return 0


def command_traverse(args: argparse.Namespace) -> int:
    document = load_graph(args.input)
    errors, warnings = validate_graph(document)
    if errors:
        write_output({"valid": False, "errors": errors, "warnings": warnings}, args.output)
        return 1
    result = traverse_graph(document, args.start, args.depth, args.relationship, args.reverse)
    write_output({"start": args.start, "paths": result}, args.output)
    return 0


def command_analyze(args: argparse.Namespace) -> int:
    document = load_graph(args.input)
    errors, warnings = validate_graph(document)
    if errors:
        write_output({"valid": False, "errors": errors, "warnings": warnings}, args.output)
        return 1
    write_output({"warnings": warnings, "analysis": analyze_graph(document)}, args.output)
    return 0


def command_agent_context(args: argparse.Namespace) -> int:
    document = load_graph(args.input)
    errors, warnings = validate_graph(document)
    if errors:
        write_output({"valid": False, "errors": errors, "warnings": warnings}, args.output)
        return 1
    result = agent_context(document, args.node, args.depth)
    result["warnings"] = warnings
    write_output(result, args.output)
    return 0
