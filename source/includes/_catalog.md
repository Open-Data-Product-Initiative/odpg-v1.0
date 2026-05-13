# Graph Catalog

The following example demonstrates a complete ODPG document connecting use cases, business objectives, KPIs, data products, governance policies, APIs, AI agents, and strategic opportunities into a unified value graph.

> Example of the catalog object usage:

```yml
schema: https://opendataproducts.org/graphs/v1/schema/graph.yaml
version: 1.0
kind: DataProductGraph
id: GRAPH-AVIATION-001
name:
  en: Aviation Data Product Value Graph

nodes:
  - id: UC-AVIATION-001
    type: UseCase
    $ref: ../usecases/predictive-maintenance-aircraft.yaml

  - id: OBJ-AVIATION-001
    type: BusinessObjective
    $ref: ../objectives/increase-fleet-availability.yaml

  - id: KPI-AVIATION-001
    type: KPI
    $ref: ../kpis/fleet-availability-rate.yaml

  - id: DP-AVIATION-001
    type: DataProduct
    $ref: ../products/aircraft-maintenance-history.yaml

  - id: DP-AVIATION-002
    type: DataProduct
    $ref: ../products/aircraft-sensor-events.yaml

  - id: API-AVIATION-001
    type: API
    $ref: ../apis/maintenance-risk-score-api.yaml

  - id: POL-AVIATION-001
    type: Policy
    $ref: ../policies/aviation-data-quality-policy.yaml

  - id: AGENT-AVIATION-001
    type: Agent
    $ref: ../agents/maintenance-recommendation-agent.yaml

  - id: OPP-AVIATION-001
    type: StrategicOpportunity
    $ref: ../opportunities/reduce-unscheduled-maintenance.yaml

edges:
  - from: UC-AVIATION-001
    to: DP-AVIATION-001
    type: uses
    confidence: high

  - from: UC-AVIATION-001
    to: DP-AVIATION-002
    type: uses
    confidence: high

  - from: UC-AVIATION-001
    to: OBJ-AVIATION-001
    type: supports
    confidence: high

  - from: DP-AVIATION-001
    to: OBJ-AVIATION-001
    type: contributesTo
    confidence: medium

  - from: DP-AVIATION-002
    to: OBJ-AVIATION-001
    type: contributesTo
    confidence: medium

  - from: KPI-AVIATION-001
    to: OBJ-AVIATION-001
    type: mesures
    confidence: high

  - from: DP-AVIATION-001
    to: KPI-AVIATION-001
    type: tracks
    confidence: medium

  - from: DP-AVIATION-001
    to: API-AVIATION-001
    type: exposes
    confidence: high

  - from: DP-AVIATION-001
    to: POL-AVIATION-001
    type: governedBy
    confidence: high

  - from: AGENT-AVIATION-001
    to: DP-AVIATION-001
    type: uses
    confidence: high

  - from: AGENT-AVIATION-001
    to: API-AVIATION-001
    type: uses
    confidence: high

  - from: UC-AVIATION-001
    to: OPP-AVIATION-001
    type: identifies
    confidence: medium

  - from: OPP-AVIATION-001
    to: OBJ-AVIATION-001
    type: alignWith
    confidence: medium
```



## Optional attributes and options

> Example of catalog metadata usage:

```yml
metadata:
  name:
    en: Aviation Data Product Value Graph
  description:
    en: Graph describing how aviation data products, use cases, policies, agents, opportunities, and business objectives are connected.
  domain:
    en: Aviation
  purpose:
    en: Support portfolio analysis, value mapping, governance review, and AI-assisted reasoning.
  tags:
    - aviation
    - predictive-maintenance
    - fleet-availability
  status: draft
  visibility: public
  owner:
    name: Aviation Data Product Team
    email: aviation-data-products@example.com
```

| Attribute                 | Type             | Description                                                                                                      |
| ------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| `metadata`                | Object           | Optional metadata block for describing the graph, its purpose, ownership, visibility, and discovery information. |
| `metadata.name`           | Object           | Human-readable name of the graph. Supports language-specific values.                                             |
| `metadata.name.en`        | String           | English name of the graph.                                                                                       |
| `metadata.description`    | Object           | Human-readable description of what the graph represents. Supports language-specific values.                      |
| `metadata.description.en` | String           | English description of the graph.                                                                                |
| `metadata.domain`         | Object           | Business, industry, or subject domain covered by the graph. Supports language-specific values.                   |
| `metadata.domain.en`      | String           | English domain name.                                                                                             |
| `metadata.purpose`        | Object           | Explanation of why the graph exists and how it should be used. Supports language-specific values.                |
| `metadata.purpose.en`     | String           | English purpose statement.                                                                                       |
| `metadata.tags`           | Array of strings | Keywords used for discovery, filtering, grouping, and search.                                                    |
| `metadata.status`         | String           | Current status of the graph. Recommended values include `draft`, `active`, `deprecated`, and `archived`.         |
| `metadata.visibility`     | String           | Intended visibility of the graph. Recommended values include `public`, `internal`, `restricted`, and `private`.  |
| `metadata.owner`          | Object           | Party responsible for the graph.                                                                                 |
| `metadata.owner.name`     | String           | Name of the owning person, team, or organization.                                                                |
| `metadata.owner.email`    | String           | Contact email for the owning party.                                                                              |
