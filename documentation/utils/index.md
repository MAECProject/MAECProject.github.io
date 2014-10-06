---
layout: flat
title: Utilities & Developer Resources
---

## Output Modification
Output modification utilities help abstract away the current MAEC XML implementation to provide alternate views for working with MAEC that either do not require XML knowledge or that translate MAEC into another standard language.

### STIX to HTML (MAEC to HTML)
<i>The `MAEC to HTML` utility to convert MAEC XML to HTML has been deprecated, and the functionality of the utility has been incorporated into the STIX-to-HTML utility.</i>

`STIX to HTML` is an XSLT stylesheet that can transform a STIX XML document (with MAEC content) into a human-readable HTML view. It was designed to be leveraged by developers, either as a mechanism for batch rendering STIX (MAEC) documents or to be embedded as a visualization component within a STIX-capable application.  Because `STIX to HTML` is an XSLT stylesheet, users must be familiar with XSLT or XSLT processing libraries/engines (e.g., Saxon or libxslt) in order to use it. 

`STIX to HTML` was created by and for developers, and therefore, customization and extension capabilities have been prioritized. Documentation on how to customize `STIX to HTML` to fit your application or operational needs can be found in the usage guide.

* [Usage Guide](https://github.com/STIXProject/stix-to-html/wiki)
* [Source Code](https://github.com/STIXProject/stix-to-html)

### MAEC to OVAL
The `MAEC to OVAL` utility converts MAEC XML into OVAL 5.7 definitions, tests, and objects.  It extracts registry key Objects and file Objects from the Actions in a MAEC Package or Bundle XML document.

The utility is at the proof of concept stage of development. 

* [Usage Guide](https://github.com/MAECProject/maec-to-oval/README)
* [Source Code](hhttps://github.com/MAECProject/maec-to-oval)

## Native MAEC Output Capabilities
MAEC modules enable other malware analysis tools to natively generate MAEC content. 

### Cuckoo Sandbox
[Cuckoo Sandbox](http://www.cuckoosandbox.org) is an automated dynamic malware analysis system.  The MAEC Cuckoo module enables Cuckoo to output MAEC output natively (i.e., the module is available as a Cuckoo "reporting" module).

* [Source Code](https://github.com/MAECProject/cuckoo)
* [Source Code](https://github.com/cuckoobox/cuckoo/tree/master/modules/reporting) (Cuckoo site)

## Translator Utilities
MAEC translator utilities enable translation of non-MAEC analysis tool output into MAEC content.

### Anubis to MAEC
[Anubis](https://anubis.iseclab.org/) is a service for analyzing malware.  Windows executables are submitted on-line to the Anubis server, and XML-based analysis reports are generated in response. 

The `Anubis to MAEC` utility generates MAEC Package output from an Anubis XML file.

* [Usage Guide](https://github.com/MAECProject/maec-to-oval/README)
* [Source Code](hhttps://github.com/MAECProject/maec-to-oval)

### ThreatAnalyzer (GFI Sandbox) to MAEC
[ThreatAnalyzer](http://www.threattracksecurity.com/enterprise-security/malware-analysis-sandbox-software.aspx) (previously known as GFI Sandbox) is a software-based, dynamic analysis sandbox for malware analysis.  

The `GFI Sandbox to MAEC` utility generates MAEC Package output from a GFI Sandbox v4 XML file.

* [Usage Guide](https://github.com/MAECProject/gfi-sandbox-to-maec/README)
* [Source Code](hhttps://github.com/MAECProject/gfi-sandbox-to-maec)

### pefile to MAEC 
[pefile](http://code.google.com/p/pefile/) is a multi-platform Python module to process PE files.  The output of pefile is useful for malware analysis.

The `pefile to MAEC` Python library converts output from the pefile utility to MAEC XML content.

* [Usage Guide](https://github.com/MAECProject/pefile-to-maec/README)
* [Source Code](https://github.com/MAECProject/pefile-to-maec)

### ThreatExpert to MAEC
[ThreatExpert](http://www.threatexpert.com/) is an automated threat analysis system.  After a malware sample is submitted through an on-line interface, the ThreatExpert system generates a threat report.

The `ThreatExpert to MAEC` utility generates MAEC Package output from a ThreatExpert XML file.  

* [Usage Guide](https://github.com/MAECProject/threatexpert-to-maec/README)
* [Source Code](https://github.com/MAECProject/threatexpert-to-maec)

### VirusTotal to MAEC
[VirusTotal](https://www.virustotal.com/) is an online service that analyses suspicious files and URLs. 

The `VT to MAEC` queries VirusTotal against an MD5 (or a file that will then be hashed) and returns the results in a MAEC Package. 

* [Usage Guide](https://github.com/MAECProject/vt-to-maec/README)
* [Source Code](https://github.com/MAECProject/vt-to-maec)

## Programmatic Support
The MAEC project develops and maintains an API to aid developers in parsing, creating, and manipulating MAEC content.

### python-maec
The `python-maec` library provides two levels of APIs to help in the creation, consumption, and manipulation of MAEC content.  

A low-level API is provided by auto-generated XML Schema-Python class bindings. Using these bindings, any MAEC content can be parsed from or written to XML, but the use of the bindings requires some knowledge of the actual MAEC schemas.

A higher-level API consists of manually designed Python classes. These "native classes" are intended to behave more like Python programmers would expect. Because they are designed manually, they currently do not support the entire MAEC standard; instead, they support only those Object types expected to be used most frequently. These "native classes" also support exporting their content as Python dictionaries and lists, which can easily be converted to JSON.  Importing from JSON is also supported.

* [Usage Guide](http://maec.readthedocs.org/)
* [Source Code](https://github.com/MAECProject/python-maec)