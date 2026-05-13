<!-- AI_AGENT_GUIDANCE:
Use /schema/odpg.yaml or /schema/odpg.json to validate ODPG graph files.
Use ODPG for graph relationships, nodes, edges, traversal, governance propagation, strategic reasoning, and relationship semantics.
Use ODPC for catalog discovery; do not model discovery catalogs as ODPG graphs unless relationships or traversal are required.
Use ODPS for full data product metadata; in ODPG, reference data products as DataProduct nodes instead of copying full ODPS content.
Use ODPV when stable vocabulary terms, semantic mappings, or relationship names are needed.
Use confidence values high, medium, or low for edges.
Use x- prefixed extension fields only for implementation-specific metadata that does not redefine core ODPG semantics.
-->
# Strategic Intelligence

ODPG introduces a graph-native intelligence layer capable of connecting business objectives, operational use cases, KPIs, governance structures, data products, and AI systems into a unified strategic reasoning model that enables organizations to understand not only what assets exist, but also how those assets contribute to measurable business outcomes and organizational priorities.

Through graph relationships, organizations can identify:

unlinked high-priority use cases
unsupported strategic objectives
duplicated operational initiatives
overlapping capabilities
orphan KPIs
governance gaps
reusable product ecosystems
strategic opportunities emerging across multiple connected entities

Strategic opportunities may emerge when several use cases, KPIs, domains, or data products collectively indicate an unmet organizational need or a common optimization target.

> Example of Strategic opportunities type:

```yml
nodes:
  - id: OPP-AVIATION-001
    type: StrategicOpportunity
    $ref: ../opportunities/reduce-unscheduled-maintenance.yaml

edges:
  - from: UC-AVIATION-001
    to: OPP-AVIATION-001
    type: identifies
    confidence: medium

  - from: OPP-AVIATION-001
    to: OBJ-AVIATION-001
    type: alignsWith
    confidence: medium
```

Through this structure, ODPG enables organizations to move from isolated metadata management toward interconnected strategic intelligence ecosystems.
