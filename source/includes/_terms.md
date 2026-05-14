<!-- AI_AGENT_GUIDANCE:
Use /schema/odpg.yaml or /schema/odpg.json to validate ODPG graph files.
Use ODPG for graph relationships, nodes, edges, traversal, governance propagation, strategic reasoning, and relationship semantics.
Use ODPC for catalog discovery; do not model discovery catalogs as ODPG graphs unless relationships or traversal are required.
Use ODPS for full data product metadata; in ODPG, reference data products as DataProduct nodes instead of copying full ODPS content.
Use ODPV when stable vocabulary terms, semantic mappings, or relationship names are needed.
Use confidence values high, medium, or low for edges.
Use x- prefixed extension fields only for implementation-specific metadata that does not redefine core ODPG semantics.
-->
# Terms used

This project works with **[Open Data Product Graphs (ODPG) 1.0](https://opendataproducts.org/odpg-v1.0/)** documents and a small HTML generator for exploration. ODPG uses the **[Open Data Product Vocabulary (ODPV)](https://opendataproducts.org/odpv-v1.0/)** as the shared vocabulary across the OpenDataProducts.org standards family: stable identifiers, labels, definitions, aliases, and relationship names should stay aligned with ODPV so graphs stay interoperable with ODPS, ODPC, and other tools.

For machine-readable lookup of vocabulary entries, use the ODPV term records at **[ODPV terms.jsonl](https://opendataproducts.org/odpv-v1.0/vocab/terms.jsonl)** when available from the publication host.

The tables below list ODPV-aligned terms this repo uses in examples, the generator, and the explorer UI, plus short notes where ODPG gives them a concrete graph shape.

## Shared terms from ODPV (graph document and nodes)

| Term (human) | ODPV-style term | Usage in this project |
| --- | --- | --- |
| Data product graph | `Graph` | Root `kind` of the YAML graph; validated in `generate_graph_explorer.py` as `Graph`. |
| Graph identifier | `Identifier` (concept) | `graph.metadata.id` and each node `id` are unique keys used by edges (`from` / `to`). |
| Reference | `Reference` (concept) | Each node's **`$ref`** property points to the underlying file or URI for that entity. |
| Data product | `DataProduct` | Node `type` value, such as sample `DP-*` nodes. |
| Use case | `UseCase` | Node `type` value, such as sample `UC-*` nodes. |
| Business objective | `BusinessObjective` | Node `type` value, such as sample `OBJ-*` nodes. |
| KPI | `KPI` | Node `type` value, such as sample `KPI-*` nodes. |
| Policy | `Policy` | Node `type` value, such as sample `POL-*` nodes; governance relationships attach here. |
| API | `API` | Node `type` value, such as sample `API-*` nodes. |
| Agent | `Agent` | Node `type` value, such as sample `AGENT-*` nodes. |
| Strategic opportunity | `StrategicOpportunity` | Node `type` value, such as sample `OPP-*` nodes. |

ODPG defines additional supported node types, such as `Domain`, `Dataset`, `Workflow`, and `Capability`, that are valid in the standard even when they do not appear in every sample graph.

## Shared relationship terms from ODPV (edges)

Edge `type` values in YAML are spelled exactly as in ODPG. The generator's core list and tooltips mirror the ODPG relationship model, including:

| Edge `type` (ODPG / ODPV-aligned) | Role in graphs here |
| --- | --- |
| `uses` | Operational usage between nodes. |
| `supports` | Support for a business objective. |
| `contributesTo` | Contribution toward an outcome or objective. |
| `measures` | KPI measures an objective or outcome. |
| `tracks` | Tracking or KPI-related information flow. |
| `dependsOn` | Dependency between nodes. |
| `produces` / `consumes` | Production or consumption of data, outputs, services, or interfaces. |
| `governedBy` | Governance or policy attachment. |
| `ownedBy` | Ownership or stewardship. |
| `alignsWith` / `alignWith` | Strategic or semantic alignment. |
| `relatedTo` | Generic semantic link. |
| `impacts` | Impact relationship. |
| `derivedFrom` | Derivation or origin. |
| `exposes` | API or interface exposure. |
| `monitors` | Monitoring relationship. |
| `identifies` | Identification of an opportunity or condition. |

Domain-specific `type` strings are allowed by ODPG for extension; the explorer will still render them, with legend coloring falling back to a neutral default when no explicit color is defined.

## ODPG- and project-specific usage notes

| Term | Description |
| --- | --- |
| `schema` | URL of the ODPG YAML schema used for validation, such as [ODPG YAML schema](https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml). |
| `version` | ODPG document version field carried in the graph root. |
| `kind` | Root document type. Use `Graph`. |
| `graph.metadata.name` | Localized graph title, such as `graph.metadata.name.en`, shown in the explorer header. |
| `graph.nodes` | Array of node objects shaped as `{ id, type, $ref }`; the explorer maps `type` to colors and groups. |
| `graph.edges` | Array of edge objects shaped as `{ from, to, type, confidence }`; `confidence` is `high`, `medium`, or `low` per ODPG guidance. |
| `generate_graph_explorer.py` | Offline generator: reads graph YAML, validates core fields, emits `graph-explorer.html` for browser viewing. |
| `graph-explorer.html` | Static visualization; relationship descriptions in the UI are aligned with the ODPG edge definitions baked into the generator. |

**Reference field name:** Use **`$ref`** on nodes when validating against the ODPG JSON/YAML schema. The generator accepts legacy `ref` values during transition, but `$ref` is the schema-aligned field.

**Relationship vocabulary:** Prefer ODPV-defined relationship identifiers for `graph.edges[].type` so the same edge semantics can be shared with ODPC, other ODPG tools, and downstream AI or governance pipelines.
