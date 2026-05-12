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