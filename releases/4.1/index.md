---
layout: flat
title: MAEC 4.1
---

This is the current release of MAEC.

**Note:** Version 4.1 is hosted on the [MAEC Legacy Site](https://maec.mitre.org/), and all files linked to below will redirect there.

### Release Notes

* Added support for [Cyber Observable eXpression (CybOX™) Version 2.1](http://cyboxproject.github.io/releases/2.1/).
* Added implementation of MAEC Capabilities, for capturing the set of high-level abilities that a malware instance may possess (please see the detailed release notes for details).
* Added ability to "label" a Malware Subject with common terms, e.g., "worm". 
* Added ability to capture details of configuration parameters used by a malware instance.
* Added ability to capture details of the development environment used in the development of a malware instance.
* Made numerous vocabulary updates, tweaks, and changes.
* There are also full [release notes](https://maec.mitre.org/language/version4.1/MAECv41releasenotes.pdf) available.

### Specifications

* [MAEC Bundle Specification, Version 4.1](https://github.com/MAECProject/specifications/blob/master/documents/PDF/MAEC_Bundle_Spec_v4_1.pdf)
* [MAEC Package Specification, Version 4.1](https://github.com/MAECProject/specifications/blob/master/documents/PDF/MAEC_Package_Spec_v2_1.pdf)
* [MAEC Container Specification, Version 4.1](https://github.com/MAECProject/specifications/blob/master/documents/PDF/MAEC_Container_Spec_v2_1.pdf)
* [MAEC Default Vocabularies Specification, Version 4.1](https://github.com/MAECProject/specifications/blob/master/documents/PDF/MAEC_Vocabs_Spec_v1_1.pdf)

### Schema Downloads

|File Name|Version|Schema|Documentation|
|---------|-------|------|-------------|
|All Files|n/a|[zip](https://maec.mitre.org/language/version4.1/maec_4.1.zip)|n/a|
|All Files (offline, with examples and documentation)|n/a|[zip](https://maec.mitre.org/language/version4.1/maec_4.1_offline.zip)|n/a|
|MAEC Bundle|4.1|[xsd](https://maec.mitre.org/language/version4.1/maec_bundle_schema.xsd)|[html](https://maec.mitre.org/language/version4.1/xsddocs/maec_bundle_schema.html)|
|MAEC Package|2.1|[xsd](https://maec.mitre.org/language/version4.1/maec_package_schema.xsd)|[html](https://maec.mitre.org/language/version4.1/xsddocs/maec_package_schema.html)|
|MAEC Container|2.1|[xsd](https://maec.mitre.org/language/version4.1/maec_container_schema.xsd)|[html](https://maec.mitre.org/language/version4.1/xsddocs/maec_container_schema.html)|
|MAEC Default Vocabularies|1.1|[xsd](https://maec.mitre.org/language/version4.1/maec_default_vocabularies.xsd)|[html](https://maec.mitre.org/language/version4.1/xsddocs/maec_default_vocabularies.html)|
|MAEC Capabilities Hierarchy Diagram|n/a|n/a|[pdf](https://maec.mitre.org/language/version4.1/MAEC_4.1_Malware_Capabilities.pdf)|

### Current Release Examples
The variety of examples below for MAEC Version 4.1 illustrate the use of MAEC Bundles, Packages, and Containers, as well as the capture of specific malware-related attributes (e.g., clustering information, AV classifications, etc.).

*IMPORTANT:* While the examples on this page are sourced from real-world analysis reports, they should be considered illustrative examples only and should not be used in real-world operations.

|File Name|Description|XML|
|---------|-----------|---|
|All Files|Archive of all v4.1 Release example files|[zip](https://maec.mitre.org/language/version4.1/maec_4.1_examples.zip)|
|Bundle Artifact|Simple Bundle capturing network traffic information|[xml](https://maec.mitre.org/language/version4.1/bundle_artifact_example.xml)|
|Bundle AV Classifications|Simple Bundle capturing Anti-Virus tool information|[xml](https://maec.mitre.org/language/version4.1/bundle_av_classifications_example.xml)|
|Bundle Candidate Indicator|Demonstrates the basic construction of a Candidate Indicator entity within a Bundle|[xml](https://maec.mitre.org/language/version4.1/bundle_candidate_indicator_example.xml)|
|Bundle Dynamic Triage Tool Output|Simple Bundle capturing dynamic analysis tool output|[xml](https://maec.mitre.org/language/version4.1/bundle_dynamic_triage_tool_output.xml)|
|Bundle Network Behavior|Simple Bundle capturing a network-based Behavior|[xml](https://maec.mitre.org/language/version4.1/bundle_network_behavior_example.xml)|
|Bundle Malicious Webpage|Demonstrates the capture of the malicious aspects of a webpage|[xml](https://maec.mitre.org/language/version4.1/bundle_malicious_webpage_example.xml)|
|Bundle Object Re-use|Demonstrates how Objects can be reused via ID references|[xml](https://maec.mitre.org/language/version4.1/bundle_object_reuse_example.xml)|
|Container Multiple Package|Demonstrates the capture of multiple Packages using a Container|[xml](https://maec.mitre.org/language/version4.1/container_multiple_package_example.xml)|
|Package Action Equivalency|Demonstrates the composition and use of an Action Equivalency entity in a Package|[xml](https://maec.mitre.org/language/version4.1/package_action_equivalency_example.xml)|
|Package Capability|Demonstrates the usage of Capabilities and Objectives in a Package, along with how they link up to Behaviors and Actions|[xml](https://maec.mitre.org/language/version4.1/package_capability_example.xml)|
|Package Capability Snifula|Provides a more detailed view of Capabilities and Objectives and their usage in characterizing a complex malware instance|[xml](https://maec.mitre.org/language/version4.1/package_capability_example_snifula.xml)|
|Package Clustering|Demonstrates how a Package can be used to capture a malware cluster (set of related malware)|[xml](https://maec.mitre.org/language/version4.1/package_clustering_example.xml)|
|Package Configuration Parameters|Demonstrates how the configuration parameters of a Malware Subject can be characterized in a Package|[xml](https://maec.mitre.org/language/version4.1/package_configuration_parameters_example.xml)|
|Package Development Environment|Demonstrates how the development environment of a Malware Subject entity can be characterized in a Package|[xml](https://maec.mitre.org/language/version4.1/package_development_environment_example.xml)|
|Package Dynamic Triage|Demonstrates how a Malware Subject entity in a Package can be used to capture multiple dynamic analysis tool outputs|[xml](https://maec.mitre.org/language/version4.1/package_dynamic_triage_example.xml)|
|Package Manual Analysis|Demonstrates how a Malware Subject entity in a Package can be used to capture manual analysis tool output|[xml](https://maec.mitre.org/language/version4.1/package_manual_analysis_example.xml)|
|Package Multi-Partite Malware|Demonstrates how multi-partite malware may be captured as unique Malware Subject entities in a Package|[xml](https://maec.mitre.org/language/version4.1/package_multi_partite_malware_example.xml)|
|Package Multiple Analysis|Demonstrates how multiple analyses for the same Malware Subject (a Zeus binary) can be combined in a single Package using multiple Analysis entities|[xml](https://maec.mitre.org/language/version4.1/package_multiple_analysis_example.xml)|
|Package Static Triage|Simple Package capturing basic static triage results|[xml](https://maec.mitre.org/language/version4.1/package_static_triage_example.xml)|

**GitHub Repository Examples**     
The [MAEC release examples](https://github.com/MAECProject/schemas/tree/master/examples), as well as examples provided by the MAEC Community, are provided at [https://github.com/MAECProject/schemas/tree/master/examples](https://github.com/MAECProject/schemas/tree/master/examples).

**STIX Examples**     
The [Structured Threat Information eXpression (STIX™) Language](http://stixproject.github.io/) can describe malware using MAEC characterizations through the use of a [MAEC schema extension](http://stix.mitre.org/XMLSchema/extensions/malware/maec_4.0.1/1.0.1/maec_4.0.1.xsd) for the [STIX TTP schema](http://stix.mitre.org/XMLSchema/ttp/1.0.1/ttp.xsd). See the "[Malware Sample](https://github.com/STIXProject/schemas/blob/version_1.0.1/samples/STIX_Malware_Sample.xml)" in the STIXProject GitHub repository for an explicit example.

**Cuckoobox Outputs**      
The [MAEC release examples](https://github.com/MAECProject/schemas/tree/master/examples) in the MAECProject GitHub repository contains example [Cuckoobox](http://www.cuckoosandbox.org/) outputs that were automatically generated and illustrate many of MAEC's features.

**MAEC Detailed Examples Document**     
The [MAEC Detailed Examples Document](https://maec.mitre.org/language/MAEC_Detailed_Examples_v4.0.1.pdf) provides comprehensive guidance on the creation of MAEC Package and Bundle documents in the context of static triage, dynamic triage, and manual analysis. Accordingly, it provides a detailed walk-through and description of a notional MAEC document for each such use case. Currently, this document is written against MAEC Version 4.0.1, though the concepts are almost completely compatible with MAEC Version 4.1.























