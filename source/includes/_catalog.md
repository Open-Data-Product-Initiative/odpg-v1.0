# Graph Catalog

The following example demonstrates a complete ODPG document connecting use cases, business objectives, KPIs, data products, governance policies, APIs, AI agents, and strategic opportunities into a unified value graph.

![Aviation Data Product Value Graph](/images/dpvg_aviation.jpeg)

> Example of the catalog object usage:

```yml
schema: https://opendataproducts.org/odpg-v1.0/schema/graph.yaml
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
    type: measures
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


## Graph Explorer Example

The following YAML example can also be used as the input for a lightweight Graph Explorer generator capable of transforming an ODPG document into an interactive HTML-based visualization. This allows organizations to convert machine-readable graph specifications into human-readable graph catalogs that can be explored visually through a browser without requiring a dedicated graph database or enterprise catalog platform.

The Graph Explorer concept is intended to demonstrate how ODPG files can serve as portable relationship intelligence structures that support governance review, strategic planning, semantic exploration, AI-agent traversal, and operational dependency analysis through standard graph visualization techniques.

A Graph Explorer implementation typically performs the following sequence of operations:

Reads the ODPG YAML file.
Validates the graph structure against the ODPG schema.
Extracts graph nodes and graph edges.
Converts the graph into a visualization-friendly structure.
Generates an interactive HTML page capable of displaying graph relationships.
Enables users to inspect node metadata, edge relationships, confidence levels, and referenced specifications.

The Graph Explorer may display:

* Data Products
* Use Cases
* Business Objectives
* KPIs
* Policies
* APIs
* Workflows
* Agents
* Strategic Opportunities

as graph nodes, while relationships such as:

* uses
* supports
* contributes_to
* governed_by
* tracks
* exposes
* identifies

can be rendered as directional graph edges.

## Python Graph Explorer Generator

A lightweight Python utility can be used to transform an ODPG YAML document into a standalone HTML Graph Explorer.

The purpose of the script is not to redefine the ODPG structure, but rather to consume the existing specification and render it visually.

The script should:

* read the ODPG YAML file
* validate required graph properties
* validate node and edge integrity
* transform graph entities into visualization structures
* generate an HTML explorer
* render the graph interactively in a browser

The script should use the standard ODPG structure exactly as defined in this specification.

![Aviation Data Product Graph Explorer](/images/graph_example.png)

> Example graph input:

```yml 
schema: https://opendataproducts.org/odpg-v1.0/schemas/graph.yaml
version: 1.0
kind: DataProductGraph
id: GRAPH-AVIATION-001
name:
  en: Aviation Data Product Value Graph

nodes:
  - id: UC-AVIATION-001
    type: UseCase
    ref: ../usecases/predictive-maintenance-aircraft.yaml

  - id: OBJ-AVIATION-001
    type: BusinessObjective
    ref: ../objectives/increase-fleet-availability.yaml

  - id: KPI-AVIATION-001
    type: KPI
    ref: ../kpis/fleet-availability-rate.yaml

  - id: DP-AVIATION-001
    type: DataProduct
    ref: ../products/aircraft-maintenance-history.yaml

  - id: DP-AVIATION-002
    type: DataProduct
    ref: ../products/aircraft-sensor-events.yaml

  - id: API-AVIATION-001
    type: API
    ref: ../apis/maintenance-risk-score-api.yaml

  - id: POL-AVIATION-001
    type: Policy
    ref: ../policies/aviation-data-quality-policy.yaml

  - id: AGENT-AVIATION-001
    type: Agent
    ref: ../agents/maintenance-recommendation-agent.yaml

  - id: OPP-AVIATION-001
    type: StrategicOpportunity
    ref: ../opportunities/reduce-unscheduled-maintenance.yaml

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
    type: measures
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
    type: alignsWith
    confidence: medium

```

## Required Dependencies & Execution

The Python implementation requires PyYAML for parsing ODPG YAML files.


1- See all options (built-in help)

```text
python generate_graph_explorer.py --help
```

You should see `-i` / `--input` and `-o` / `--output` with their defaults.

---
2- Run this 

```
python generate_graph_explorer.py -i "/path/to/graph.yml" -o "/path/to/explorer.html"
```

| Script | Purpose |
|---|---|
| [`generate_graph_explorer.py`](https://github.com/Open-Data-Product-Initiative/odpg-v1.0/blob/main/scripts/generate_graph_explorer.py) | Transform the graph yaml file into HTML file |

The script read the **graph.yaml** file and generates **graph-explorer.html** file. The resulting HTML file can then be opened directly in a browser to explore the ODPG graph visually.

## Quick reference

| Flag | Meaning |
|------|--------|
| `-i PATH` or `--input PATH` | ODPG graph YAML file to read |
| `-o PATH` or `--output PATH` | HTML file to write |
| `-h` or `--help` | Show help and defaults |

**Defaults:** if you omit `-i`, the script uses `graph.yaml` **in the same directory as** `generate_graph_explorer.py`. If you omit `-o`, it writes **`graph-explorer.html`** in the **current working directory**.

## Graph Explorer Capabilities

A generated Graph Explorer implementation may support:

* node visualization
* edge visualization
* relationship labels
* confidence display
* node grouping by type
* graph zooming and panning
* graph traversal
* dependency inspection
* governance inspection
* AI-agent relationship visualization
* clickable specification references

The Graph Explorer demonstrates how ODPG specifications can become both machine-readable and human-navigable while preserving interoperability with the broader Open Data Products ecosystem.