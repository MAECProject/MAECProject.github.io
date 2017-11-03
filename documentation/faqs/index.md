---
layout: flat
title: Frequently Asked Questions (FAQs)
---

### <a href="#a">General</a>
<ul style="font-weight:normal; font-size:100%; list-style:none">

<li><a href="#a1">A1. What is MAEC?</a></li>
<li><a href="#a2">A2. How is &quot;MAEC&quot; pronounced?</a></li>
<li><a href="#a3">A3. Why and how was MAEC developed?</a></li>
<li><a href="#a4">A4. Is MAEC a formal standard?</a></li>
<li><a href="#a5">A5. How is MAEC licensed?</a></li>
<li><a href="#a6">A6. How can I get involved? How can I make contributions to MAEC development?</a></li>
</ul>

### <a href="#b">MAEC Language</a>
<ul style="font-weight:normal; font-size:100%; list-style:none">
<li><a href="#b1">B1. Where can I get the current version of MAEC?</a></li>
<li><a href="#b2">B2. Is a specification available for the MAEC Language?</a></li>
<li><a href="#b3">B3. Where can I find examples of what I can capture and do with MAEC?</a></li>
<li><a href="#b4">B4. What tools or utilities are available to help me use or develop MAEC content?</a></li>
<li><a href="#b5">B5. Is there a GUI of some sort that will help me select MAEC elements?</a></li>
<li><a href="#b6">B6. Are there plans to support other forms of data interchange for MAEC (e.g., YAML, etc.)?</a></li>
<li><a href="#b7">B7. Where can I find examples of MAEC data? Are there any MAEC repositories?</a></li>
<li><a href="#b8">B8. What is included in a MAEC release?</a></li>
</ul>

### <a href="#c">Using MAEC</a>
<ul style="font-weight:normal; font-size:100%; list-style:none">
<li><a href="#c1">C1. Why are so many things optional in MAEC?</a></li>
<li><a href="#c2">C2. What if I need to define something that isn&#39;t part of the MAEC schema?</a></li>
<li><a href="#c3">C3. Can the same information be captured in multiple places in MAEC?</a></li>
</ul>

### <a href="#d">Relationships to Other Efforts</a>
<ul style="font-weight:normal; font-size:100%;list-style:none">
<li><a href="#d1">D1. What is the relationship between MAEC and STIX?</a></li>
<li><a href="#d2">D2. When would STIX be used to capture malware information and when would MAEC be used?</a></li>
<li><a href="#d3">D3. What is the relationship between MAEC and TAXII?</a></li>
</ul>

### <a href="#e">MAEC Community</a>
<ul style="font-weight:normal; font-size:100%;list-style:none">
<li><a href="#e1">E1. What is the role of the MAEC Community and how can I join?</a></li>
<li><a href="#e2">E2. What is MITRE's role in MAEC? How long does MITRE plan to maintain it?</a></li>
<li><a href="#e3">E3. Who sponsors MAEC? What is the relationship between MAEC and DHS?</a></li>
</ul>

### <a name="a"></a>General

#### <a name="a1"></a> A1. What is MAEC?

[Malware Attribute Enumeration and Characterization (MAEC™)](/releases/5.0) is a structured language for encoding and communicating high fidelity information about malware based upon attributes such as behaviors, artifacts, and relationships between malware samples.

#### <a name="a2"></a> A2. How is "MAEC" pronounced?

MAEC is pronounced as "mike." This pronunciation stems from classical Latin, in which the diphthong 'ae' is pronounced as a long 'i'. Examples of other words that use the same pronunciation are maestro and alumnae.

#### <a name="a3"></a> A3. Why and how was MAEC developed?

MAEC was developed to eliminate the ambiguity and inaccuracy that currently exists in malware descriptions. By reducing reliance on signatures, MAEC aims to improve human-to-tool, tool-to-tool, and tool-to-human communication about malware; allow for faster development of countermeasures by enabling the ability to leverage responses to previously observed malware instances; and reduce potential duplication of malware analysis efforts by researchers.

MAEC is a community-developed effort and has received input from members of various communities, including those from industry, academia, and government. [The MITRE Corporation](https://www.mitre.org/) maintains MAEC and its public website presence and provides impartial technical guidance to the [MAEC Community](/community) throughout the process to ensure MAEC serves the public interest. MAEC is sponsored by the office of [Cybersecurity and Communications](https://www.dhs.gov/office-cybersecurity-and-communications/) at the [U.S. Department of Homeland Security](https://www.dhs.gov/).

#### <a name="a4"></a> A4. Is MAEC a formal standard?

MAEC is not currently being pursued in a formal standards body. However, once an appropriate level of maturity, stability, and use is achieved, international standardization may be sought.

#### <a name="a5"></a> A5. How is MAEC licensed?

See the "License" section of the [Terms of Use](/Legal).

#### <a name="a6"></a> A6. How can I get involved? How can I make contributions to MAEC development?
There are several opportunities to get involved. See the [MAEC Community](/community) page for details, or contact us directly at [maec@mitre.org](mailto:maec@mitre.org). 

### <a name="b"></a> MAEC Language

#### <a name="b1"></a> B1. Where can I get the current version of MAEC?

The current version of the Malware Attribute Enumeration and Characterization (MAEC™) Language is available on the [Current Release](/releases/5.0) page. In addition, non-normative JSON schemas and examples are available in the [MAECProject GitHub repository](https://github.com/MAECProject/schemas).

#### <a name="b2"></a> B2. Is a specification available for the MAEC Language?

See the [Specifications](https://maecproject.github.io/releases/5.0/#specifications) section on the [Current Release](/releases/5.0) page.

#### <a name="b3"></a> B3. Where can I find examples of what I can capture and do with MAEC?

Examples can be found in the [MAECProject repository](https://github.com/MAECProject/schemas/tree/master/examples) on GitHub.com. Additional examples are given in the [MAEC 5.0 Core Specification](https://maecproject.github.io/releases/5.0/MAEC_Core_Specification.pdf).

#### <a name="b4"></a> B4. What tools or utilities are available to help me use or develop MAEC content?
MAEC can be manipulated manually or programmatically. If using MAEC manually, such as to capture malware analysis results, no tools are provided. Use of a JSON editor is recommended. 

For programmatic development and use, some MAEC scripts and translator utilities are hosted in separate [MAECProject GitHub repositories](https://github.com/MAECProject/).

Also see [MAEC Supporters](/community/supporters/) for a list of vendors that have implemented MAEC in their products or services. 

#### <a name="b5"></a> B5. Is there a GUI of some sort that will help me select MAEC elements?
A GUI is not available, however, such a tool could be available in the future.

#### <a name="b6"></a> B6. Are there plans to support other forms of data interchange for MAEC (e.g., YAML, etc.)?
No. Rather than producing additional MAEC serializations or a formal implementation-independent specification, MAEC concepts will likely be migrated into the [Structured Threat Information Expression (STIX™)](https://oasis-open.github.io/cti-documentation/) 2.x Malware Object.

#### <a name="b7"></a> B7. Where can I find examples of MAEC data? Are there any MAEC repositories?
Visit the [Current Release](/releases/5.0) page for additional information. 

At present, there are no public repositories of MAEC data, nor are there plans by MITRE to establish one. However, community members interested in hosting a MAEC data repository are encouraged to do so. 

#### <a name="b8"></a> B8. What is included in a MAEC release?
[MAEC 5.0](/releases/5.0) includes two specification documents (core concepts and vocabularies) and a corresponding set of non-normative JSON schemas and examples.

### <a name="c"></a> Using MAEC
Some of the FAQs in this section are somewhat technical in nature. Please refer to the [MAEC Language Specifications](/releases/5.0/#specifications) for further information.

#### <a name="c1"></a> C1. Why are so many things optional in MAEC?
Many properties are optional in MAEC to make the language as flexible as possible, enabling users to capture exactly what they want and nothing more.

#### <a name="c2"></a> C2. What if I need to define something that isn't part of the MAEC schema?
MAEC cannot be directly customized, but because a MAEC Package can include relevant [Structured Threat Information Expression (STIX™)](https://oasis-open.github.io/cti-documentation/) Observable Objects, custom STIX Properties and Objects can be used to capture some content that is not defined in MAEC. 

In addition, the MAEC development team encourages the community to engage in the ongoing discussion so that new properties can be defined and integrated into future versions of MAEC as necessary. Please consider participating in the [MAEC Community](/community) to help with the development of MAEC. 

#### <a name="c3"></a> C3. Can the same information be captured in multiple places in MAEC?
In earlier versions of MAEC, it was possible to express the same concept in multiple ways, but rather than being a feature, the flexibility led to confusion. [MAEC 5.0](/releases/5.0/) recognizes the need for flexibility, but also recognizes the importance of simplicity, standardization, and reduced optionality. Therefore, MAEC 5.0 aims to have a single way of capturing any particular facet of malware information. 

### <a name="d"></a> Relationships to Other Efforts

#### <a name="d1"></a> D1. What is the relationship between MAEC and STIX?
The MAEC Language directly imports and uses components of the OASIS [Structured Threat Information eXpression (STIX™)](https://oasis-open.github.io/cti-documentation/) language. More specifically, MAEC’s malware characterization relies on the common implementation (structure and content) that STIX Cyber Observables provide for expressing cyber observables. Thus, whereas MAEC provides coverage of malware analysis context, behaviors, and capabilities, STIX Cyber Observables provide the underpinnings necessary to broadly cover objects, such as files and network connections, used in the context of malware.

#### <a name="d2"></a> D2. When would STIX be used to capture malware information and when would MAEC be used?
MAEC is targeted toward malware analysts, and therefore provides a comprehensive, structured way of capturing detailed information about malware samples. By contrast, [STIX](https://oasis-open.github.io/cti-documentation/) targets a more diverse audience by capturing a broad spectrum of cyber-threat related information, including basic malware information. Consequently, an organization performing cyber threat analysis must consider their specific use case to determine whether the extensive malware characterization ability of MAEC or the more basic STIX Malware Object is most appropriate.

#### <a name="d3"></a> D3. What is the relationship between MAEC and TAXII?
The OASIS [Trusted Automated eXchange of Indicator Information (TAXII™)](https://oasis-open.github.io/cti-documentation/) defines a set of services and message exchanges for securely sharing automated cyber threat information. Most commonly, TAXII uses [STIX](https://oasis-open.github.io/cti-documentation/) to represent cyber threat information where STIX characterizes <i>what</i> is being shared and TAXII defines <i>how</i> the STIX payload is shared. However, TAXII could use MAEC as its payload instead of STIX.

### <a name="e"></a> MAEC Community

#### <a name="e1"></a> E1. What is the role of the MAEC Community and how can I join?
The [MAEC Community](/community) includes representatives from antivirus vendors, operating system vendors, software vendors, IT users, security services providers, and others from across the international cyber security community who have come together to help build this growing, open-source industry effort. 

There are multiple options available for involvement including participating in the conversations
on our [dedicated email discussion list](/community/#discussion-lists--archives), contributing to the [Encyclopedia of Malware Attributes](https://collaborate.mitre.org/ema/index.php/ema:Main_Page) on MITRE’s collaboration website, and/or contributing to the development of [MAEC tools and utilities](/community/#tool--utility-development) on GitHub.

Visit the [MAEC Community](/community) page to learn more or to [join](/community) the MAEC effort.

#### <a name="e2"></a> E2. What is MITRE's role in MAEC? How long does MITRE plan to maintain it?
The [MITRE Corporation (MITRE)](https://www.mitre.org/) manages and maintains the development of the MAEC Language, MAEC website, community engagement, and discussion lists to enable open and public collaboration with all stakeholders and provides neutral guidance throughout the process to ensure that MAEC serves the public interest.     

In accordance with its mission, MITRE has traditionally acted in the public interest. Its unique role allows it to provide an objective perspective to this effort. MITRE will maintain MAEC as long as it serves the community to do so.

#### <a name="e3"></a> E3. Who sponsors MAEC? What is the relationship between MAEC and DHS?
MAEC is a DHS-led and sponsored effort of the office of [Cybersecurity and Communications](https://www.dhs.gov/office-cybersecurity-and-communications/) at the [U.S. Department of Homeland Security (DHS)](https://www.dhs.gov/). [MITRE](https://www.mitre.org/), operating as DHS's Federally Funded Research and Development Center (FFRDC), manages the development of the MAEC Language, this MAEC website, community engagement, and discussion lists to enable open and public collaboration with all stakeholders.
