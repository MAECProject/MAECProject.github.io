---
layout: flat
title: About MAEC
---

[Malware Attribute Enumeration and Characterization (MAEC™)](/releases/5.0) (pronounced “mike”) is a community-developed structured language for encoding and sharing high-fidelity information about malware based upon attributes such as behaviors, artifacts, and relationships between malware samples.

By eliminating the ambiguity and inaccuracy that currently exists in malware descriptions and by reducing reliance on signatures, MAEC aims to: 

* Enable correlation, integration, and automation.
* Improve human-to-human, human-to-tool, tool-to-tool, and tool-to-human communication about malware.
* Allow for the faster development of countermeasures by enabling the ability to leverage responses to previously observed malware instances.
* Reduce potential duplication of malware analysis efforts by researchers.

## Malware

Malicious software—also called "malware"—is responsible for a variety of malicious activities, ranging from spam email distribution via botnets to the theft of sensitive information via targeted social engineering attacks. Effectively an autonomous agent operating on behalf of an attacker, malware can perform any action that can be expressed in code, and consequently, poses a significant threat to cybersecurity..

Therefore, the protection of computer systems from malware is a primary cybersecurity concern for organizations and individuals, as even a single instance of uncaught malware can result in damaged systems and compromised data. 

To date, the majority of anti-malware efforts focus on early detection, where the most common methods are based on physical signatures and heuristics. While often effective, such methods have significant drawbacks. For example, signatures are unsuitable for dealing with zero-day, targeted, polymorphic, and other forms of emerging malware. Similarly, heuristic detection may generically detect certain types of malware, but it will miss those for which it does not have a pattern, such as kernel-level rootkits. Therefore, these methods cannot be exclusively relied upon to deal with the current influx of malware.

## Why MAEC

### Problem

Modern methods for detecting and combating malware often rely on the characterization of malware attributes and behaviors. 

Typically, such behaviors and attributes are discovered via static and dynamic analysis techniques. The combination of the two allows for an encompassing profile of malware to be constructed based upon the malware’s disassembled binary and observed run-time behavior. 

Before [MAEC](/releases/5.0), the lack of an accepted standard for unambiguously characterizing malware meant there was no clear method for communicating the specific malware attributes detected in malware by the analyses, nor for enumerating its fundamental makeup. The results included non-interoperable and disparate malware reporting between organizations, disjointed or inaccurate malware attribution, the duplication of malware analysis efforts, increased difficulty in determining the severity of a malware threat, and a greater delay between malware infection and detection/response.

### Solution

[MAEC](/releases/5.0) solves these problems. The characterization of malware using abstract patterns offers a wide range of benefits over the useage of physical signatures, and allows for the accurate encoding of how malware operates and the specific actions that it performs. Such information can not only be used for malware detection, but also for assessing the malware’s end-goal the malware is pursuing and the corresponding threat that it represents. 

Focusing on the attributes and behaviors of malware facilitates detection and analysis of emerging, sophisticated malware threats that circumvent the traditional signature-based and heuristic approaches. Characterizing malware in a standard way supports collaboration across organizations and the identification of common behavior, functionality, and code bases across instances of malware. 

## The MAEC Language

The MAEC Language is defined by [two specification documents](http://maecproject.github.io/releases/5.0/#specifications). The core concepts document introduces MAEC, provides high-level use cases, and defines MAEC data types and top-level objects. The vocabularies document provides explicit values for each of the open vocabularies referenced in the core concepts document. In addition, non-normative [JSON schemas and examples](http://maecproject.github.io/releases/5.0/#json-schemas) are available on the [MAEC Project GitHub repository](https://github.com/MAECProject/schemas).

The MAEC schema was developed to enable analysts to capture a full gamut of information about malware. However, a MAEC Package is valid with minimal information. It is only necessary to define four properties: the type (“package”), a unique identifier, the MAEC schema version, and one MAEC Object. All other properties are optional.

Learn about the [MAEC Language](/documentation/overview/), or go to the [current release](/releases/5.0).

## Benefits

The adoption of MAEC for encoding high-fidelity information about malware has major benefits for the community:

* **Elimination of ambiguity and inaccuracy in malware descriptions** – MAEC improves human-to-human, human-to-tool, tool-to-tool, and tool-to-human communication about anti-malware related information. This will positively impact all major stakeholders, including producers and consumers of malware analysis and related malware data, as well as the end-users of tools for malware prevention and mitigation.     
      
* **Reduced duplication of malware analysis efforts** – A common method of characterizing malware, along with a corresponding standard for malware analysis reporting, will allow researchers and analysts to determine whether a particular malware instance has already been analyzed.     
     
* **Improved general awareness of malware** – A widely adopted standard for characterizing malware will allow for increased public awareness of malware threats and activity.     
     
* **Decreased overall response time to malware threats** – MAEC’s standard method of describing malware behavior will enable countermeasures for previously observed malware instances to be leveraged, resulting in faster mitigation and response.    

## MAEC Community

The [MAEC Community](/community) includes representatives from antivirus vendors, operating system vendors, software vendors, IT users, security services providers, and others from across the international cyber security community who have come together to help build this growing, open-source industry effort. 

A few short cuts: 

* **[MAEC Community Discussion List](/community#discussion-lists--archives)** – Where community members discuss the latest versions of the MAEC specifications, schemas, utilities, and other items integral to the ongoing development of MAEC.      
     
* **[Encyclopedia of Malware Attributes](/community/#encyclopedia-of-malware-attributes)** – Where the MAEC Community collaborates on building our semantic mediawiki of malware capabilities, behaviors, and structural features, and their associated attributes.    
     
* **[MAECProject GitHub Tools & Utilities](https://github.com/MAECProject/)** – The central location for MAEC Community members to make open-source contributions to MAEC development and manage issue tracking for the MAEC schemas, utilities, and other supporting information and items.     

Feedback is welcome at [maec@mitre.org](mailto:maec@mitre.org).
