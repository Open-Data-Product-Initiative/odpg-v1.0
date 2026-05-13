---
title: Open (source) Data Product Graphs DRAFT | Linux Foundation

language_tabs: # must be one of https://git.io/vQNgJ
- yaml

toc_footers:
  - License <a href='https://www.apache.org/licenses/LICENSE-2.0'>Apache 2.0</a>
  - <br/><a href='https://opendataproducts.org'>Specification home</a>
  - <br/>Linux Foundation</a>

includes:
  - structure
  - catalog
  - nodes
  - edges
  - confidence
  - strategy
  - governance
  - interoperability
  - toolkit
  - extensions
  - terms
  - contributors

search: true

code_clipboard: true

meta:
  - name: description
    content: The Data Product Graphs Specification is a vendor-neutral, machine-readable graph model for managing data products, use cases, business objectives, KPIs, and their relationships. It defines the nodes, edges, attributes, and structures needed to connect data product lifecycle management with measurable business value.

---

# OPEN DATA PRODUCT GRAPHS - The Linux Foundation


## Version DRAFT

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in BCP 14 ([RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) and [RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174)) when, and only when, they appear in all capitals, as shown here.

The specification is shared under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
Development of the specification is under the umbrella of the Linux Foundation.


| Topic            | Link                                                                                                | Description                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Version source   | [Open Data Product Graphs 1.0 on GitHub](https://github.com/Open-Data-Product-Initiative/odpg-v1.0) | Official source repository for the ODPG 1.0 specification     |
| ODPG YAML schema | [YAML Schema](https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml)                             | Machine-readable schema definition in YAML format             |
| ODPG JSON schema | [JSON Schema](https://opendataproducts.org/odpg-v1.0/schema/odpg.json)                             | Machine-readable schema definition in JSON format             |
| Contribute       | [Raise an issue in GitHub](https://github.com/Open-Data-Product-Initiative/odpg-v1.0/issues)        | Submit issues or suggestions to the specification maintainers |


## Introduction

Modern organizations increasingly operate across highly distributed ecosystems composed of data products, APIs, workflows, governance controls, AI systems, analytical capabilities, business domains, and operational processes that collectively contribute to strategic business execution. Despite significant investments in data platforms and governance programs, many organizations still struggle to understand how technical assets connect to business value because metadata, governance, strategy, and operational context are often managed independently from one another.

Traditional metadata catalogs primarily focus on technical discovery, indexing, and lineage management, which makes them valuable for inventory and governance use cases but insufficient for understanding the broader strategic relationships that exist between business objectives, operational capabilities, AI systems, data products, and measurable outcomes.

**Open Data Product Graphs ODPG-v1.0** addresses this challenge by introducing a machine-readable graph specification that enables organizations to describe and manage the relationships between interconnected entities across the enterprise ecosystem, thereby transforming isolated specifications into connected intelligence structures capable of supporting governance reasoning, strategic alignment, semantic interoperability, AI traversal, impact analysis, and reusable data ecosystems.


Through ODPG, organizations can represent questions such as:

- Which use cases depend on this data product?
- Which business objectives are supported by this use case?
- Which KPIs are measured through these data products?
- Which data products contribute to the same strategic objective?
- Which AI agents are consuming these APIs?
- Which policies govern this workflow or domain?
- Which business areas contain unsupported strategic objectives?
- Which strategic opportunities emerge from multiple related use cases?

By enabling organizations to describe these relationships using a standardized graph structure, ODPG provides the foundation for graph-native enterprise intelligence ecosystems.

## Relationship to the Open Data Products Specification Family

The Open Data Products specification family consists of interoperable standards that collectively support the lifecycle, governance, semantics, discovery, interoperability, and intelligence of data ecosystems, where each specification focuses on a specific responsibility while remaining interoperable with the others.

![Open Data Product Graphs overview diagram](/images/odpg.jpeg)

| Specification	| Role |
|---|---| 
| ODPS | Defines the structure and specification of a data product |
| ODPV | Defines shared vocabulary and semantic meaning |
| ODPC | Defines catalog interoperability and discovery structures |
| ODPG | Defines graph relationships between data products, use cases, objectives, policies, and related entities |

Within this ecosystem, ODPS defines the product structure itself, ODPV defines semantic consistency and shared meaning, ODPC defines discovery and catalog interoperability, while ODPG defines the graph relationships that connect those specifications into an interconnected enterprise ecosystem capable of supporting strategic intelligence and machine reasoning.

As a result, ODPG should be understood as the relationship and intelligence layer of the Open Data Products ecosystem because it provides the contextual structure necessary for understanding how different enterprise assets connect to each other operationally, strategically, semantically, and organizationally.

## Purpose

The purpose of ODPG is to provide organizations with a standardized machine-readable graph specification that enables them to model relationships between data products, business objectives, operational use cases, governance structures, APIs, workflows, AI systems, and strategic capabilities in a consistent and interoperable manner.

Through this graph model, organizations can establish visibility into how data products contribute to business outcomes, how governance policies propagate across interconnected assets, how AI agents interact with enterprise systems, how KPIs align with strategic goals, and how operational dependencies affect downstream capabilities.

ODPG therefore enables organizations to:

* connect use cases to data products
* connect data products to business objectives
* represent strategic contribution paths
* model governance relationships
* support impact analysis
* identify strategic gaps and overlaps
* support semantic traversal
* enable AI reasoning across enterprise ecosystems
* support graph-native interoperability
* provide reusable relationship intelligence structures
