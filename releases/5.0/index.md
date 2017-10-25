---
layout: flat
title: MAEC 5.0
---

This is the current release of MAEC.

Feedback or questions about this release are welcome on the [MAEC Community Email Discussion List](http://maecproject.github.io/community/#discussion-lists--archives), or directly to [maec@mitre.org](mailto:maec@mitre.org).      

### Release Notes

The most significant changes in the MAEC 5.0 release include: a more graph-based approach through the definition of MAEC top-level objects and MAEC relationships; JSON serialization, which significantly reduces the size and complexity of MAEC documents and allows for better integration with other applications; a single standardized output format (the MAEC Package); a new object for capturing properties associated with malware families; a new type for capturing metadata about signatures and rules (e.g., YARA rules) triggered by a malware instance; and a new type for capturing details of how a malware instance is obfuscated. A complete list of changes is available in Section 1.2 of the MAEC 5.0 "Core" Specification.

This release of MAEC 5.0 includes the following:     

* MAEC 5.0 "Core" Specification
* MAEC 5.0 "Vocabularies" Specification
* A full set of JSON schemas that correspond with the specifications
* A Cuckoo Sandbox 2.x reporting module that produces native MAEC 5.0 output  

### Specifications     

* [MAEC Core Specification, Version 5.0](/releases/5.0/MAEC_Core_Specification.pdf)
* [MAEC Vocabularies Specification, Version 5.0](/releases/5.0/MAEC_Vocabularies_Specification.pdf)

### JSON Schemas     

* [JSON schemas, MAEC Version 5.0](https://github.com/MAECProject/schemas)

### Cuckoo Reporting Modules     

The Cuckoo Sandbox 2.x reporting module produces native MAEC 5.0 output.

* Main module: [https://github.com/MAECProject/cuckoo/blob/maec5.0-cuckoo2.0/cuckoo/reporting/maecreport.py](https://github.com/MAECProject/cuckoo/blob/maec5.0-cuckoo2.0/cuckoo/reporting/maecreport.py)
* API Call mappings: [https://github.com/MAECProject/cuckoo/blob/maec5.0-cuckoo2.0/cuckoo/reporting/maec_api_call_mappings.json]( https://github.com/MAECProject/cuckoo/blob/maec5.0-cuckoo2.0/cuckoo/reporting/maec_api_call_mappings.json)

