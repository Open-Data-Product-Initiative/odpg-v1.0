<!-- AI_AGENT_GUIDANCE:
Use /schema/odpg.yaml or /schema/odpg.json to validate ODPG graph files.
Use ODPG for graph relationships, nodes, edges, traversal, governance propagation, strategic reasoning, and relationship semantics.
Use ODPC for catalog discovery; do not model discovery catalogs as ODPG graphs unless relationships or traversal are required.
Use ODPS for full data product metadata; in ODPG, reference data products as DataProduct nodes instead of copying full ODPS content.
Use ODPV when stable vocabulary terms, semantic mappings, or relationship names are needed.
Use confidence values high, medium, or low for edges.
Use x- prefixed extension fields only for implementation-specific metadata that does not redefine core ODPG semantics.
-->
# Governance and Trust

ODPG supports governance propagation by enabling organizations to connect policies, controls, ownership structures, quality requirements, stewardship responsibilities, and compliance expectations directly to graph entities and relationships.

This graph-native governance model enables organizations to understand how governance requirements propagate across interconnected assets and how changes to policies, ownership, or controls may impact downstream systems, use cases, APIs, workflows, or AI agents.

```yml 
nodes:
  - id: DP-AVIATION-001
    type: DataProduct
    $ref: ../products/aircraft-maintenance-history.yaml

  - id: POL-AVIATION-001
    type: Policy
    $ref: ../policies/aviation-data-quality-policy.yaml

edges:
  - from: DP-AVIATION-001
    to: POL-AVIATION-001
    type: governedBy
    confidence: high
```

This governance structure supports:

* policy traceability
* governance impact analysis
* stewardship visibility
* trust scoring
* lifecycle governance
* AI-safe access management
* explainable governance reasoning
* compliance auditing
