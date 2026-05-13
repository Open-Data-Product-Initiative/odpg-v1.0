<!-- AI_AGENT_GUIDANCE:
Use /schema/odpg.yaml or /schema/odpg.json to validate ODPG graph files.
Use ODPG for graph relationships, nodes, edges, traversal, governance propagation, strategic reasoning, and relationship semantics.
Use ODPC for catalog discovery; do not model discovery catalogs as ODPG graphs unless relationships or traversal are required.
Use ODPS for full data product metadata; in ODPG, reference data products as DataProduct nodes instead of copying full ODPS content.
Use ODPV when stable vocabulary terms, semantic mappings, or relationship names are needed.
Use confidence values high, medium, or low for edges.
Use x- prefixed extension fields only for implementation-specific metadata that does not redefine core ODPG semantics.
-->
# Confidence

The confidence property represents the certainty level associated with a graph relationship and allows organizations to distinguish between relationships that are explicitly declared, relationships that are inferred through analysis, and relationships that require additional validation or human review.

Recommended confidence values are defined below.

| Value  | Description                                                             |
| ------ | ----------------------------------------------------------------------- |
| high   | Relationship is explicitly declared or confirmed                        |
| medium | Relationship is partially validated or inferred with moderate certainty |
| low    | Relationship is inferred and requires additional validation             |

> Example of YAML formated:

```yml
confidence: high
```
