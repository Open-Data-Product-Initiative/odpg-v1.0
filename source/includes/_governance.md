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
