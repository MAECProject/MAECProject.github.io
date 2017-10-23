---
layout: flat
title: MAEC Overview
---

The goal of [Malware Attribute Enumeration and Characterization (MAEC™)](/releases/5.0), pronounced “mike,” is to provide a basis for transforming malware research and response. MAEC aims to eliminate the ambiguity and inaccuracy that currently exists in malware descriptions and to reduce reliance on signatures. In this way, MAEC seeks to transform malware research and response by improving communication, reducing potential duplication of malware analysis efforts, and allowing for faster development of countermeasures by enabling the ability to leverage responses to previously observed malware instances.

## The MAEC Language

[MAEC](/releases/5.0) is a standardized language for sharing structured information about malware. The MAEC data model can be represented as a connected graph of nodes and edges where MAEC top level objects define the nodes and MAEC relationships define the edges. A relationship is a link between MAEC objects that describes how the objects are related.

As shown in the diagram, MAEC defines several top-level objects: Behaviors, Malware Actions, Malware Families, Malware Instances, and Collections. Relationships between objects (including [Structured Threat Information Expression (STIX™](https://oasis-open.github.io/cti-documentation/)) cyber observable objects) are depicted by directed edges in the diagram: embedded relationships (those that are specified directly on a top-level object as an object property) are labeled in black font (labels correspond to the property names), and direct relationships are labeled using a blue background (labels correspond to literal values for the relationship type).      

<img src="maec_top_level_objects.png" alt="MAEC Top Level Objects" class="text-align:center" height="495" width="950"/>  

See the [MAEC Core Specification](/releases/5.0/MAEC_Core_Specification.pdf) for detailed information about top-level objects and direct and embedded relationships.
      
## Example

The example MAEC Package shown below captures results of static analysis performed with the PEiD tool on a malware instance. 

Even without a formal understanding of the MAEC data model, it should be clear that the information captured includes the entry point and subsystem defined in the PE headers of the file, as well as the version of the linker used in linking the code. 

**NOTE:** Additional examples are given in the [MAEC Core Specification](/releases/5.0/MAEC_Core_Specification.pdf) and on the [Use Cases](/documentation/use_cases/) page.
<img src="maec_example.png" alt="MAEC Example" class="text-align:center" height="1000" width="860"/>
