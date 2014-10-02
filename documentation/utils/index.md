---
layout: flat
title: Utilities & Developer Resources
---

## Output Formatting
Output formatting utilities help abstract away the MAEC XML to provide different views for working with MAEC that may not require XML knowledge or that translate MAEC into another standard language.

### MAEC to HTML
The `MAEC to HTML` utility converts MAEC XML to HTML.

### MAEC to OVAL
The `MAEC to OVAL` utility converts MAEC XML to OVAL XML.

## Native Analysis Capabilities
MAEC native analysis modules and tools enable other tools to natively generate MAEC content. 

### Cuckoo Sandbox
Cuckoo Sandbox is an automated dynamic malware analysis system.  This MAEC module enables Cuckoo to output MAEC output natively.

* [Source Code](https://github.com/MAECProject/cuckoo)

## Translator Utilities
MAEC translator utilities enable translation of non-MAEC tool output into MAEC content.

### Anubis to MAEC
The `Anubis to MAEC` utility generates MAEC Package output from an [Anubis](http://anubis.iseclab.org) XML file.

Compatibility:  MAEC schema v4.1 and CybOX 2.1

### GFI Sandbox to MAEC
The `GFI Sandbox to MAEC` utility generates MAEC Package output from a GFI Sandbox v4 XML file.

Compatibility:  MAEC schema v4.1 and CybOX 2.1

### pefile to MAEC 
The `pefile to MAEC` utility...

* Compatibility:  MAEC v4.1 and CybOX 2.1  
* Dependencies:  [python-maec](https://github.com/MAECProject/python-maec), [python-cybox](https://github.com/CybOXProject/python-cybox)
* [Source Code](https://github.com/MAECProject/pefile-to-maec)

### ThreatExpert to MAEC

The `ThreatExpert to MAEC` utility generates MAEC Package output from a ThreatExpert XML file.  

Compatibility:  MAEC schema v4.1 and CybOX 2.1

* [Source Code](https://github.com/MAECProject/threatexpert-to-maec)

### VirusTotal to MAEC

The `VT to MAEC` utility generates MAEC output from a VirusTotal report.  

Compatibility:  MAEC v4.1 and CybOX 2.1  

* [Source Code](https://github.com/MAECProject/vt-to-maec)

## Programmatic Support
The MAEC project develops and maintains APIs which aid developers in parsing, creating, and manipulating MAEC content.

### Python APIs (python-maec)

The `python-maec` APIs provide machine-generated bindings and higher-level APIs that aid in the creation, consumption, and manipulation of MAEC content.

* [Source Code](https://github.com/MAECProject/python-maec)