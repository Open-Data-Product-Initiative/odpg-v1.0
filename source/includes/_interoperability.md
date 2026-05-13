# AI Agent Interoperability

ODPG provides structured graph context that can be consumed by AI agents, automation systems, semantic search engines, orchestration platforms, and reasoning systems operating across enterprise ecosystems.

Through graph traversal, AI agents can identify:

* which data products are relevant to a task
* which APIs are available
* which objectives are being supported
* which policies apply
* which governance boundaries exist
* which dependencies affect execution
* which relationships are inferred versus confirmed

```yml 
nodes:
  - id: AGENT-AVIATION-001
    type: Agent
    $ref: ../agents/maintenance-recommendation-agent.yaml

  - id: DP-AVIATION-001
    type: DataProduct
    $ref: ../products/aircraft-maintenance-history.yaml

  - id: API-AVIATION-001
    type: API
    $ref: ../apis/maintenance-risk-score-api.yaml

edges:
  - from: AGENT-AVIATION-001
    to: DP-AVIATION-001
    type: uses
    confidence: high

  - from: AGENT-AVIATION-001
    to: API-AVIATION-001
    type: uses
    confidence: high
```

This capability establishes the foundation for graph-native AI ecosystems where agents can navigate enterprise knowledge structures using trusted semantic relationships and governance-aware graph traversal.

## Interoperability

ODPG is designed to operate as an interoperable relationship layer across the broader Open Data Products ecosystem, where graph nodes may reference ODPS data products, ODPV vocabulary definitions, ODPC catalog entries, governance specifications, APIs, workflows, use cases, KPI definitions, or external organizational assets.

The ref property enables ODPG to link graph entities to external specifications while maintaining lightweight graph portability and reusable interoperability structures.

```yml
$ref: ../products/aircraft-maintenance-history.yaml
```

Through this interoperability model, ODPG enables organizations to federate graph ecosystems across teams, domains, platforms, and organizations while maintaining semantic consistency and reusable relationship intelligence.