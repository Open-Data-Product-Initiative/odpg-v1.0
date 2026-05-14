<!-- AI_AGENT_GUIDANCE:
Use /schema/odpg.yaml or /schema/odpg.json to validate ODPG graph files.
Use ODPG for graph relationships, nodes, edges, traversal, governance propagation, strategic reasoning, and relationship semantics.
Use ODPC for catalog discovery; do not model discovery catalogs as ODPG graphs unless relationships or traversal are required.
Use ODPS for full data product metadata; in ODPG, reference data products as DataProduct nodes instead of copying full ODPS content.
Use ODPV when stable vocabulary terms, semantic mappings, or relationship names are needed.
Use confidence values high, medium, or low for edges.
Use x- prefixed extension fields only for implementation-specific metadata that does not redefine core ODPG semantics.
-->
# Specification Structure

> Example of details object usage:

```yml
schema: https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml
version: 1.0
kind: Graph
graph:
  metadata:
    id: GRAPH-AVIATION-001
    name:
      en: Aviation Data Product Value Graph
    description:
      en: Graph describing how aviation data products, use cases, policies, agents, opportunities, and business objectives are connected.
  nodes: []
  edges: []
```

An ODPG document consists of a standardized graph structure composed of metadata, graph nodes, and graph edges, where the graph itself represents a connected ecosystem of business, operational, technical, governance, and AI-related entities.

The root structure of an ODPG document is defined as follows:

## Mandatory attributes

The following root properties are defined within an ODPG document.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `schema` | URL | Yes | URL of the ODPG schema used for validation |
| `version` | String or number | Yes | Version of the ODPG specification |
| `kind` | String | Yes | Type of graph specification document. Must be `Graph` |
| `graph` | Object | Yes | Container for graph metadata, nodes, and edges |
| `metadata` | Object | Yes | Metadata describing the graph |
| `metadata.id` | String | Yes | Unique identifier of the graph |
| `metadata.name` | Object | Yes | Human-readable graph name using language-specific values |
| `metadata.name.en` | String | Yes |  English name of the graph.  |
| `metadata.description` | Object | Yes | Human-readable graph description using language-specific values |
| `metadata.description.en` | String | Yes | English description of the graph. |
| `nodes` | Array of node objects | Yes | Collection of graph node objects |
| `edges` | Array of edge objects | Yes | Collection of graph edge objects |

## Optional attributes and options

> Example of catalog metadata usage:

```yml
schema: https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml
version: 1.0
kind: Graph
graph:
  metadata:
    id: GRAPH-AVIATION-001
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
  nodes: []
  edges: []
```

| Attribute                 | Type             | Description                                                                                                      |
| ------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
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
