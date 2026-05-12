# Specification Structure

An ODPG document consists of a standardized graph structure composed of metadata, graph nodes, and graph edges, where the graph itself represents a connected ecosystem of business, operational, technical, governance, and AI-related entities.

The root structure of an ODPG document is defined as follows:

> Example of details object usage:

```yml
schema: https://opendataproducts.org/odpg-v1.0/schema/graph.yaml
version: 1.0
kind: DataProductGraph
id: GRAPH-AVIATION-001
name:
  en: Aviation Data Product Value Graph
nodes: []
edges: []
```


## Root Properties

The following root properties are defined within an ODPG document.

| Property	| Description|
|---|---|
| **schema** |	URL of the ODPG schema used for validation |
| **version**	| Version of the ODPG specification |
| **kind**	| Type of graph specification document |
| **id**	| Unique identifier of the graph |
| **name**	| Human-readable graph name |
| **nodes**	| Collection of graph nodes |
| **edges**	| Collection of graph edges |