---
layout: flat
title: Frequently Asked Questions (FAQs)
---

### <a href="#a">General</a>
<ul style="font-weight:normal; font-size:100%; list-style:none">

<li><a href="#a1">A1. What is MAEC?</a></li>
<li><a href="#a2">A2. How is &quot;MAEC&quot; pronounced?</a></li>
<li><a href="#a3">A3. Is a specification available for the MAEC Language?</a></li>
<li><a href="#a4">A4. Where can I find examples of what I can capture and do with MAEC?</a></li>
<li><a href="#a5">A5. Why was MAEC developed?</a></li>
<li><a href="#a6">A6. How was MAEC developed?</a></li>
<li><a href="#a7">A7. Where can I get MAEC?</a></li>
<li><a href="#a8">A8. Is MAEC a formal standard?</a></li>
<li><a href="#a9">A9. How is MAEC licensed?</a></li>
<li><a href="#a10">A10. How can my organization and I get involved?</a></li>
<li><a href="#a11">A11. How can I make contributions to MAEC development?</a></li>
<li><a href="#a12">A12. How do I submit questions related to this effort?</a></li>
<li><a href="#a13">A13. What is MAEC Compatibility?</a></li>
<li><a href="#a14">A14. Is someone from MAEC available to speak or participate on panel discussion at industry-related events, meetings, etc.?</a></li>
</ul>

### <a href="#b">MAEC Language</a>
<ul style="font-weight:normal; font-size:100%; list-style:none">
<li><a href="#b1">B1. What is included in a MAEC release?</a></li>
<li><a href="#b2">B2. What tools or utilities are available to help me use or develop MAEC content?</a></li>
<li><a href="#b3">B3. Is there a GUI of some sort that will help me select MAEC elements?</a></li>
<li><a href="#b4">B4. Are there plans to support other forms of data interchange for MAEC (e.g., JSON, YAML, etc.)?</a></li>
<li><a href="#b5">B5. Where can I find examples of MAEC data? Are there any MAEC repositories?</a></li>
</ul>

### <a href="#c">Using MAEC</a>
<ul style="font-weight:normal; font-size:100%; list-style:none">
<li><a href="#c1">C1. MAEC seems complicated – is it too expansive for my use?</a></li>
<li><a href="#c2">C2. Why are so many things optional in MAEC?</a></li>
<li><a href="#c3">C3. How does the xsi:type extension mechanism work?</a></li>
<li><a href="#c4">C4. What if I need to define something that isn&#39;t part of the 
MAEC schema?</a></li>
<li><a href="#c5">C5. Can the same information be captured in multiple places in 
MAEC?</a></li>
</ul>

### <a href="#d">Relationships to Other Efforts</a>
<ul style="font-weight:normal; font-size:100%;list-style:none">
<li><a href="#d1">D1. What is the relationship between MAEC and CybOX?</a></li>
<li><a href="#d2">D2. What is the relationship between MAEC and STIX?</a></li>
<li><a href="#d3">D3. When would STIX be used to capture malware information and when would MAEC be used?</a></li>
<li><a href="#d4">D4. What is the relationship between MAEC and TAXII?</a></li>
</ul>

### <a href="#e">MAEC Community</a>
<ul style="font-weight:normal; font-size:100%;list-style:none">
<li><a href="#e1">E1. What is the role of the MAEC Community and how can I join?</a></li>
<li><a href="#e2">E2. What is MITRE?</a></li>
<li><a href="#e3">E3. What is MITRE&#39;s role in MAEC?</a></li>
<li><a href="#e4">E4. Why is MITRE maintaining MAEC, and how long does MITRE plan to maintain it?</a></li>
<li><a href="#e5">E5. Who pays for MAEC? Who is the Sponsor?</a></li>
<li><a href="#e6">E6. What is the relationship between MAEC and DHS?</a></li>
</ul>

### <a name="a"></a>General

####<a name="a1"></a> A1. What is MAEC?

Malware Attribute Enumeration and Characterization (MAEC™) is a structured language for encoding and communicating high fidelity information about malware based upon attributes such as behaviors, artifacts, and attack patterns.

#### <a name="a2"></a> A2. How is "MAEC" pronounced?

MAEC is pronounced as "mike." This pronunciation stems from classical Latin, in which the diphthong 'ae' is pronounced as a long 'i'. Examples of other words that use the same pronunciation are maestro and alumnae.

#### <a name="a3"></a> A3. Is a specification available for the MAEC Language?

Both PDF and Word versions of the current [MAEC Language Specifications](https://github.com/MAECProject/specifications) are available.

#### <a name="a4"></a> A4. Where can I find examples of what I can capture and do with MAEC?

Examples can be found in the [MAEC Schemas MAECProject repository](https://github.com/MAECProject/schemas/tree/master/examples) on GitHub.com.

#### <a name="a5"></a> A5. Why was MAEC developed?

MAEC was developed to eliminate the ambiguity and inaccuracy that currently exists in malware descriptions. By reducing reliance on signatures, MAEC aims to improve human-to-tool, tool-to-tool, and tool-to-human communication about malware; allow for faster development of countermeasures by enabling the ability to leverage responses to previously observed malware instances; and reduce potential duplication of malware analysis efforts by researchers.

#### <a name="a6"></a> A6. How was MAEC developed?

MAEC is a community-developed effort and has received input from members of various communities, including those from industry, academia, and government. [The MITRE Corporation](http://www.mitre.org/) maintains MAEC and its public website presence and provides impartial technical guidance to the [MAEC Community]() throughout the process to ensure MAEC serves the public interest. MAEC is sponsored by the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the [U.S. Department of Homeland Security](http://www.dhs.gov/).

#### <a name="a7"></a> A7. Where can I get MAEC?

The current MAEC schema, as well as example files, schematron rules, and related documentation, are available in the [MAEC Schemas in the MAECProject repository](https://github.com/MAECProject/schemas) on GitHub.com.

#### <a name="a8"></a> A8. Is MAEC a formal standard?

MAEC is not currently being pursued in a formal standards body. However, once an appropriate level of maturity, stability, and use is achieved, international standardization will be sought.

#### <a name="a9"></a> A9. How is MAEC licensed?

See the "[License]()" section of the [Terms of Use]().

#### <a name="a10"></a> A10. How can my organization and I get involved?
There are several opportunities to get involved. The [MAEC Community Email Discussion List]() is where community members discuss the latest drafts of the MAEC schemas, utilities and other items integral to the ongoing development of MAEC. 

The [MAEC Development Group](https://handshake.mitre.org/) on MITRE's Handshake collaboration Web site allows the [MAEC Community]() to more easily share and revise information and files and to post items such as example content in a more secure environment. Please email [maec@mitre.org](mailto:maec@mitre.org) to join the Handshake group. 

Visit the [MAEC Community]() page for additional information. 

#### <a name="a11"></a> A11. How can I make contributions to MAEC development?
The [MAECProject repositories](https://github.com/MAECProject/) on GitHub.com are the central location for [MAEC Community]() members to make open-source contributions to MAEC development and manage issue tracking for the MAEC schemas, utilities, and other supporting information and items. Please visit the [MAECProject GitHub repositories](https://github.com/MAECProject/) or email [maec@mitre.org](mailto:maec@mitre.org) for further information.

#### <a name="a12"></a> A12. How do I submit questions related to this effort?
We encourage you to submit questions to the general [MAEC Community Email Discussion List]() which we actively read and monitor. You may also submit questions directly to [maec@mitre.org](mailto:maec@mitre.org) if you do not wish to hold the discussion in a public venue.

#### <a name="a13"></a> A13. What is MAEC Compatibility?
[MAEC Compatibility]() provides for a product, service, or repository to be reviewed and registered as officially "MAEC-Compatible," thereby assisting organizations in understanding and leveraging the three different types of capabilities that can leverage the [MAEC Language](). 

If your organization uses or is planning to use MAEC, please refer to the [MAEC Compatibility Program]() and [How to Make a Declaration]() for instructions on how to participate, and/or contact [maec@mitre.org](mailto:maec@mitre.org) for additional information. 

#### <a name="a14"></a> A14. Is someone from MAEC available to speak or participate on panel discussion at industry-related events, meetings, etc.?
Yes, contact [maec@mitre.org](mailto:maec@mitre.org) to have the MAEC Team present a briefing or participate in a panel discussion about MAEC and/or information sharing at your event.

### <a name="b"></a> MAEC Language

#### <a name="b1"></a> B1. What is included in a MAEC release?
A MAEC release includes individually-versioned MAEC schemas (i.e., Bundle, Package, and Container schemas) and the latest versions of the independently-versioned MAEC vocabulary schemas. 

MAEC releases are packaged in two different ways: 
<ol>
<li>A zipped bundle to support local development, with local references and including copies of all imported or utilized schemas.</li>
<li>A zipped bundle to support development with Internet access, with only remote references to imported schemas.</li>
</ol> 
Additionally, a version is hosted on [maec.mitre.org]() to enable validation. 

#### <a name="b2"></a> B2. What tools or utilities are available to help me use or develop MAEC content?
MAEC can be manipulated manually or programmatically. If using MAEC manually, such as to capture malware analysis results, no tools are currently provided, but use of an XML editor is recommended. 

For programmatic development and use, some MAEC scripts and translator utilities are hosted in separate [MAECProject GitHub repositories](https://github.com/MAECProject/). In addition, a Python API for parsing, manipulating, and generating MAEC content is hosted in the [MAECProject Python-MAEC GitHub repository](https://github.com/MAECProject/python-maec). 

#### <a name="b3"></a> B3. Is there a GUI of some sort that will help me select MAEC elements?
A GUI is not available at this time, but such a tool could be available in the future.

#### <a name="b4"></a> B4. Are there plans to support other forms of data interchange for MAEC (e.g., JSON, YAML, etc.)?
Yes. Eventually, a formal MAEC implementation-independent specification will be produced, to include guidance for developing technology-specific implementations such as JavaScript Object Notation (JSON), Resource Description Framework (RDF)/Web Ontology Language (OWL), YAML Ain't Markup Language (YMAL), or other implementations. XML was used in the initial release to enable rapid development and implementation.

#### <a name="b5"></a> B5. Where can I find examples of MAEC data? Are there any MAEC repositories?
See the [Examples](https://maec.mitre.org/language/examples.html) page on this MAEC Web site. 

At present, there are no public repositories of MAEC data, nor are there plans by MITRE to establish one. However, community members interested in hosting a MAEC data repository are strongly encouraged to do so. 

### <a name="c"></a> Using MAEC
Some of the FAQs in this section are somewhat technical in nature. Please refer to the "MAEC Language Specification" on the Documents page of this website for further information.

#### <a name="c1"></a> C1. MAEC seems complicated – is it too expansive for my use?
The MAEC schema was developed to enable analysts to capture a full gamut of information about malware. However, a MAEC Bundle is valid with very little information: it is only necessary to define a unique identifier and to specify the MAEC schema version. All other fields are optional.

#### <a name="c2"></a> C2. Why are so many things optional in MAEC?
Aside from a unique identifier and the MAEC schema version, all objects are optional in MAEC. This was done to make the language as flexible as possible: a user is able to capture exactly what they want and nothing more.

#### <a name="c3"></a> C3. How does the xsi:type extension mechanism work?
The xsi:type XML schema extension mechanism works by allowing for the substitution of types that are created as derivatives of an existing abstract type. As such, one must simply include the xsi:type attribute on an element that uses the parent abstract type, and accordingly specify the name of the type that one wishes to substitute for this element inside this attribute. For example, if one wishes to use the FileObj:FileObjectType type from [Cyber Observables Expression (CybOX™)](https://cybox.mitre.org/) in the Properties element (which uses the abstract cyboxCommon:ObjectPropertiesType) of the Malware Instance Object Attributes in a MAEC Bundle, they would specify the xsi:type attribute on this element with the name of the object type inside: 

&lt;maecBundle:Malware_Instance_Object_Attributes&gt;<br>
&lt;cybox:Properties xsi:type=&quot;FileObj:FileObjectType&quot;&gt;<br>
&lt;FileObj:File_Name&gt;dg003_improve_8080_V132.exe&lt;/FileObj:File_Name&gt;<br>
&lt;FileObj:Size_In_Bytes&gt;196608&lt;/FileObj:Size_In_Bytes&gt;<br>
&lt;/cybox:Properties&gt;<br>
&lt;/maecBundle:Malware_Instance_Object_Attributes&gt;

#### <a name="c4"></a> C4. What if I need to define something that isn't part of the MAEC schema?
MAEC is very flexible and can accommodate custom fields and objects. For example, one can use the Custom Properties/Property fields at the root level of the larger [Cyber Observables Expression (CybOX™)](https://cybox.mitre.org/) ObjectType specify a set of custom attributes that are not defined elsewhere. Accordingly, it is possible to define a new type of CybOX Object that can then be plugged into the Property field of the CybOX ObjectType using the xsi:type extension mechanism (e.g., xsi:type="CustomObj:CustomObjectType"). 

In addition, the MAEC development team encourages the community to engage in the ongoing discussion so that new fields and fields can be defined and integrated into future versions of MAEC as necessary. Please consider joining the public MAEC Community Email Discussion List and/or the MAEC Development Group on Handshake (email [maec@mitre.org](mailto:maec@mitre.org) to request access). 

#### <a name="c5"></a> C5. Can the same information be captured in multiple places in MAEC?
Yes. MAEC is very flexible and there are often a multiple places that the same characterized information, e.g., a particular Action or Behavior, can be captured.

### <a name="d"></a> Relationships to Other Efforts

#### <a name="d1"></a> D1. What is the relationship between MAEC and CybOX?
The [Cyber Observable eXpression (CybOX™)](https://cybox.mitre.org/) is a related [U.S. Department of Homeland Security](http://www.dhs.gov/)–led effort of the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) that provides a structured language for describing elements within the cyber operational environment. MAEC uses components of the CybOX language for characterizing cyber observables associated with malware. In particular, MAEC makes use of CybOX's Object and Action fields (which are extended in MAEC's MalwareActionType type) to characterize malware-related system artifacts and low-level behaviors, respectively.

#### <a name="d2"></a> D2. What is the relationship between MAEC and STIX?
The [Structured Threat Information eXpression (STIX™)](https://stix.mitre.org/) is a related [U.S. Department of Homeland Security](http://www.dhs.gov/)–led effort of the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) to characterize a rich set of cyber threat information in a standardized and structured manner. STIX can describe malware using MAEC characterizations through use of the MAEC schema extension for the TTP schema and can also characterize indicators in a fashion similar to MAEC's Candidate Indicators.

#### <a name="d3"></a> D3. When would STIX be used to capture malware information and when would MAEC be used?
[Structured Threat Information eXpression (STIX™)](https://stix.mitre.org/) is used to describe high-level cyber threat information to include indicators, as well as information about threat actors, campaigns, incidents, and other related entities. On the other hand, MAEC is used to describe malware attributes of one or more malware instances at various levels of abstraction. Certainly, there is overlap between the two languages, particularly when it comes to capturing indicator information (e.g., file sizes, file hashes) through the common use of [Cyber Observable eXpression (CybOX™)](https://cybox.mitre.org/). 

While there are no definite rules for what is most appropriately captured with MAEC versus STIX, MAEC will typically be used to capture malware information that is gathered through the analysis process, and STIX will be used to capture information related to the interpretation of the analysis results in a broader, threat-based context. For example, while MAEC would capture the particular details of the behaviors and artifacts associated with a malware instance, STIX would be used to capture additional details regarding the particular threat actors that may make use of the malware instance. Thus, when malware analysis information beyond simple indicator information is to be captured by STIX, the STIX schema extension for MAEC should be used to leverage the MAEC data model. 

#### <a name="d4"></a> D4. What is the relationship between MAEC and TAXII?
The [Trusted Automated eXchange of Indicator Information (TAXII™)](http://taxii.mitre.org/) is a related [U.S. Department of Homeland Security](http://www.dhs.gov/)–led effort of the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) to define a set of services and message exchanges for securely sharing automated cyber threat information. TAXII uses [Structured Threat Information eXpression (STIX™)](https://stix.mitre.org/) to represent cyber threat information in a standardized and structured manner (STIX characterizes what is being shared, while TAXII defines how the STIX payload is shared). STIX is one payload that TAXII can convey, and STIX can describe malware using MAEC.

### <a name="e"></a> MAEC Community

#### <a name="e1"></a> E1. What is the role of the MAEC Community and how can I join?
The [MAEC Community](https://maec.mitre.org/community/index.html) comprises members from across the international cyber security community who have come together to help build MAEC. There are multiple options available for involvement:

<ul>
<li>The <a href="https://maec.mitre.org/community/discussionlist.html">MAEC Community Email Discussion List</a> is where community members discuss the latest drafts of the MAEC schemas, utilities, and other items integral to the ongoing development of MAEC. </li>

<li>The <a href="https://github.com/MAECProject">MAECProject GitHub repositories</a> are the central location for MAEC Community members to make open-source contributions to MAEC tool and API development and manage issue tracking for the MAEC schemas, utilities, and other supporting information and items. </li>

<li>The <a href="https://handshake.mitre.org/">MAEC Development Group</a> on MITRE's Handshake collaboration Web site allows the MAEC Community to more easily share and revise information and files and to post items such as example content in a more secure environment. To join Handshake and the MAEC Development group, please email us at maec@mitre.org for an invitation. </li>
</ul>

For more information on the community and how to join, please visit the [MAEC Community](https://maec.mitre.org/community/index.html) page. 

#### <a name="e2"></a> E2. What is MITRE?
In partnership with government clients, [The MITRE Corporation](http://www.mitre.org/) (MITRE) is a not-for-profit corporation working in the public interest. It addresses issues of critical national importance, combining systems engineering and information technology to develop innovative solutions that make a difference. 

MITRE's work is focused within Federally Funded Research and Development Centers (FFRDCs) for the Department of Defense, Federal Aviation Administration, Internal Revenue Service and Department of Veterans Affairs, Department of Homeland Security, Administrative Office of the U.S. Courts; and the Centers for Medicare and Medicaid Services. 

#### <a name="e3"></a> E3. What is MITRE's role in MAEC?
[MITRE](http://www.mitre.org/) manages the development of the MAEC Language, MAEC Web site, community engagement, and discussion lists to enable open and public collaboration with all stakeholders.

#### <a name="e4"></a> E4. Why is MITRE maintaining MAEC, and how long does MITRE plan to maintain it?
In accordance with its mission, [MITRE](http://www.mitre.org/) has traditionally acted in the public interest. Its unique role allows it to provide an objective perspective to this effort. MITRE will maintain MAEC as long as it serves the community to do so.

#### <a name="e5"></a> E5. Who pays for MAEC? Who is the Sponsor?
MAEC is sponsored by the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security.

#### <a name="e6"></a> E6. What is the relationship between MAEC and DHS?
MAEC is a [U.S. Department of Homeland Security](http://www.dhs.gov/)–led effort of the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/). 

[The MITRE Corporation](http://www.mitre.org/), operating as DHS's Federally Funded Research and Development Center (FFRDC), manages the development of the MAEC Language, MAEC Web site, community engagement, and discussion lists to enable open and public collaboration with all stakeholders. 



