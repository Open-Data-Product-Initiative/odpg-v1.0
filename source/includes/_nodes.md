# Nodes

The nodes section defines the entities included within the graph, where each node represents a resource, capability, objective, policy, product, workflow, dataset, or system participating in the ecosystem being modeled.

A node may represent an internal resource defined directly within the organization or an external specification referenced through another machine-readable file.

Instead of embedding full resource definitions directly into the graph, ODPG encourages interoperability through references using the ref property, thereby enabling organizations to connect graph structures with ODPS documents, ODPV vocabularies, governance artifacts, APIs, workflows, use cases, or external specifications.

```yml 
nodes:
  - id: UC-AVIATION-001
    type: UseCase
    ref: ../usecases/predictive-maintenance-aircraft.yaml

  - id: OBJ-AVIATION-001
    type: BusinessObjective
    ref: ../objectives/increase-fleet-availability.yaml

  - id: DP-AVIATION-001
    type: DataProduct
    ref: ../products/aircraft-maintenance-history.yaml
```
 ## Node Properties

Each node within an ODPG document represents a distinct entity participating in the graph ecosystem, where the node itself serves as the graph reference point that enables relationships, dependencies, semantic mappings, governance propagation, strategic alignment, and interoperability across connected specifications and platforms.

The following properties are defined for graph nodes.

| Property	| Description |
|---|---|
| id	| Unique identifier of the node |
| type	| Type of graph entity represented by the node |
| ref	| Path or URI to the referenced specification or resource |

The id property uniquely identifies the node within the graph and allows edges to establish relationships between connected entities.

The type property identifies the category of entity represented by the node, thereby enabling graph consumers, validation systems, governance engines, AI agents, and traversal engines to interpret the role of the entity correctly.

The ref property provides a path or URI reference to the underlying specification, thereby allowing ODPG to function as a lightweight relationship layer that interoperates with external specifications such as ODPS documents, governance definitions, API specifications, vocabulary definitions, use case files, or objective specifications.

## Supported Node Types

ODPG supports multiple node types capable of representing strategic, operational, governance, semantic, and AI-related entities across enterprise ecosystems.

| Node Type            | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| DataProduct          | A data product defined using ODPS or compatible structures  |
| UseCase              | A business, analytical, operational, or AI-related use case |
| BusinessObjective    | A strategic business objective or organizational goal       |
| KPI                  | A measurable business or operational indicator              |
| Domain               | A business, organizational, technical, or data domain       |
| Dataset              | A structured or unstructured dataset                        |
| API                  | A service interface exposed or consumed by a data product   |
| Policy               | A governance, compliance, security, or quality policy       |
| Workflow             | A business or technical workflow                            |
| Agent                | An AI agent or automation actor                             |
| Capability           | A business or technical capability                          |
| StrategicOpportunity | An inferred or declared strategic opportunity               |


The node model is intentionally extensible so that organizations can expand graph structures with additional node types while preserving interoperability with the core ODPG structure.