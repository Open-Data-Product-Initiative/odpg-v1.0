# Specification extensions

While the Open Data Product Graphs Specification defines the core graph objects and attributes, organizations may need to add implementation-specific metadata for local tools, internal workflows, or platform-specific requirements.

Extension properties are implemented as patterned fields that are always prefixed with `x-`. These fields may appear in ODPG objects such as the graph root, `metadata`, `metadata.owner`, `nodes`, and `edges`.

Extensions are not part of the official ODPG object model unless they are later adopted into the specification. Tooling may ignore extension fields unless explicit support has been added.

Extensions should not be used to redefine core ODPG semantics. They should be used only for additional metadata that does not fit the standard attributes.

Useful and widely adopted extensions may become candidates for future versions of the standard. To propose useful extensions, raise an issue in GitHub:

[Open Data Product Initiative GitHub issues](https://github.com/Open-Data-Product-Initiative/odpg-v1.0/issues)

> Example of extension usage:

```yml
schema: https://opendataproducts.org/odpg-v1.0/schema/graph.yaml
version: 1.0
kind: DataProductGraph
id: GRAPH-AVIATION-001
name:
  en: Aviation Data Product Value Graph
x-internal-id: foobar123
x-source-system: internal-graph-platform

metadata:
  owner:
    name: Aviation Data Product Team
    email: aviation-data-products@example.com
    x-team-id: TEAM-042

nodes:
  - id: DP-AVIATION-001
    type: DataProduct
    $ref: ../products/aircraft-maintenance-history.yaml
    x-lineage-system-id: lin-987

edges:
  - from: DP-AVIATION-001
    to: OBJ-AVIATION-001
    type: contributesTo
    confidence: medium
    x-evidence-url: https://example.com/evidence/graph-aviation-001
```

| <div style="width:150px">Element name</div> | Type | Options | Description |
| --- | --- | --- | --- |
| **^x-** | any |  | Allows extensions to the Open Data Product Graphs Schema. The field name MUST begin with `x-`, for example, `x-internal-id`. The value can be null, a primitive, an array, or an object. |
