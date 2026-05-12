# Edges

The edges section defines the relationships between nodes, where each edge establishes a directional connection that represents strategic alignment, operational dependency, semantic association, governance propagation, usage patterns, contribution paths, ownership relationships, or interoperability mappings between entities.

An edge always connects a source node to a target node using the from and to properties.
```yml
edges:
  - from: UC-AVIATION-001
    to: DP-AVIATION-001
    type: USES
    confidence: high

  - from: UC-AVIATION-001
    to: OBJ-AVIATION-001
    type: SUPPORTS
    confidence: high

  - from: DP-AVIATION-001
    to: OBJ-AVIATION-001
    type: CONTRIBUTES_TO
    confidence: medium
```
Through edges, ODPG enables organizations to construct connected value graphs capable of supporting strategic analysis, governance reasoning, graph traversal, semantic interoperability, dependency analysis, and AI-driven contextual reasoning.

## Edge Properties

Each edge within an ODPG graph contains properties that describe the relationship connecting two nodes.
| Property   | Description                          |
| ---------- | ------------------------------------ |
| from       | Source node identifier               |
| to         | Target node identifier               |
| type       | Relationship type                    |
| confidence | Confidence level of the relationship |

The **from** property identifies the source node from which the relationship originates.

The **to** property identifies the destination node receiving the relationship.

The **type** property defines the semantic meaning of the relationship.

The **confidence** property defines the certainty level associated with the relationship, thereby enabling organizations and AI systems to distinguish between explicitly declared relationships and inferred or partially validated relationships.

## Supported Edge Types

ODPG supports multiple relationship types capable of representing operational, strategic, governance, semantic, and AI-related connections between graph entities.
| Edge Type      | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| USES           | A node uses another node as part of execution or operation    |
| SUPPORTS       | A node supports a business objective                          |
| CONTRIBUTES_TO | A node contributes toward an outcome or objective             |
| MEASURES       | A KPI measures an objective or outcome                        |
| TRACKS         | A node tracks or provides KPI-related information             |
| DEPENDS_ON     | A node depends on another node                                |
| PRODUCES       | A node produces data, outputs, or services                    |
| CONSUMES       | A node consumes data, APIs, or outputs                        |
| GOVERNED_BY    | A node is governed by a policy or control                     |
| OWNED_BY       | A node is owned by a person, team, or domain                  |
| ALIGNS_WITH    | A node aligns strategically or semantically with another node |
| RELATED_TO     | A generic semantic relationship                               |
| IMPACTS        | A node impacts another node                                   |
| DERIVED_FROM   | A node originates from another node                           |
| EXPOSES        | A node exposes an API or interface                            |
| MONITORS       | A node monitors another node                                  |
| IDENTIFIES     | A node identifies an opportunity or condition                 |

The relationship model is designed to remain extensible so that organizations can introduce domain-specific relationship types while maintaining compatibility with the core ODPG graph structure.