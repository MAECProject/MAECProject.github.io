---
layout: flat
title: Suggested Practices
---

This page contains suggested practices (sometimes called best practices) for producing and consuming MAEC content. Following these practices will ensure the best conformance with the design goals of MAEC and the best compatibility with other MAEC tools. These are not requirements, however: in some cases, technical or business requirements will mean you can't comply with them and that's fine. Think of them as "do it this way unless you have a good reason not to".

## General Practices

General practices apply across MAEC (and sometimes CybOX).

### Formatting IDs

MAEC IDs are [XML QNames](http://en.wikipedia.org/wiki/QName). Each ID includes both a namespace portion (optional) and an ID portion (required) separated by a colon (:). The recommend approach to creating MAEC IDs is to define a producer namespace and namespace prefix, then use the form:

`[ns prefix]:[construct type]-[GUID]`

The "ns prefix" should be a namespace prefix bound to a namespace owned/controlled by the producer of the content.

Some examples:

    acme:package-ce431003-ad07-4c96-bd7a-a50a3196e2a0
    acme:bundle-bf8bc5d5-c7e6-46b0-8d22-7500fea77196
    acme:behavior-79090715-8d6a-46b7-943b-c0bb9e063788

In order to use this approach, you will need to define that namespace prefix in the head of your XML document:

```xml
<maec:MAEC_Package xmlns:acme="http://acme.example.com" ...
```

This format provides high assurance that IDs will be both unique and meaningful, because the producer namespace denotes who's producing it, the construct name denotes what it is, and the overall ID including the GUID lends a high degree of confidence in its uniqueness.

### Assigning IDs

MAEC has a number of constructs that REQUIRE the assignment of IDs in order to be schema-valid:

* [Package](/data-model/{{site.current_version}}/maecPackage/PackageType)
* [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType)
* [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType)
* [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType)
* [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType)
* [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType)
* [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType)
* [Candidate Indicator](/data-model/{{site.current_version}}/maecBundle/CandidateIndicatorType)
* [Behavior Collection](/data-model/{{site.current_version}}/maecBundle/BehaviorCollectionType)
* [Action Collection](/data-model/{{site.current_version}}/maecBundle/ActionCollectionType)
* [Object Collection](/data-model/{{site.current_version}}/maecBundle/ObjectCollectionType)
* [Candidate Indicator Collection](/data-model/{{site.current_version}}/maecBundle/CandidateIndicatorCollectionType)

Accordingly, MAEC extends or makes direct use of a number of CybOX entities. In these entities, the assignment of IDs is not required as in MAEC; however, we highly recommend assigning IDs for these constructs, for consistency with the MAEC-defined constructs and also potential re-use and referencing:

* [Malware Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType)
* [CybOX Object](/data-model/{{site.current_version}}/cybox/ObjectType)

## MAEC-Specific Practices

The following practices are specific to MAEC.

### Recommended Properties

The MAEC schema was developed to enable analysts to capture a full gamut of information about malware. However, a MAEC Bundle or Package is valid with very little information: it is only necessary to define a unique identifier and to specify the MAEC schema version. While all other properties in MAEC are optional, it is recommended that the following fields are captured:

* Malware Instance Object Attributes field - this field should be used to provide the MAEC Bundle or Package recipient with the information they require about the malware instance object. Note that the Malware Instance Object Attributes field is defined both in the Bundle (BundleType) and in the Malware Subject of a Package (MalwareSubjectType).  The definitions are equivalent; however, the BundleType's Malware Instance Object Attributes field should only be used if the Bundle is used in a stand-alone fashion.  Otherwise, only the Package MalwareSubjectType's Malware Instance Object Attributes field should be used (note that when a Bundle is embedded in a Package, the defined_subject field of the Bundle must be set to 'false').

* Grouping Relationships field - Malware Subject relationship information should be provided for Packages that contain more than one Malware Subject. For example, the Grouping Relationships field might be used to indicate that the a Package contains several Zeus variants.

### Object References
Objects used in MAEC can be represented as embedded Objects (defined and nested inside of the fields that uses them) or as separate Objects (referenced from multiple Actions using the idref attribute).  The following recommendations are made:

* In cases where multiple Actions reference the same Object, the Object should be defined separately and referenced from each Action. For example, if one Action creates a file, and another Action reads from the same file, it is recommended that the file Object is created once and then referenced by both Actions rather than being defined twice. Aside from reducing file size, referencing separately defined Objects means that any changes or additions to the Objects' content only need to be made in one location.

* An embedded Object should be used to define the Malware Subject in the Malware_Instance_Object_Attributes field.

### Tool References

Typically, tool information should be defined in line within an Analysis field using the Tool field (of ToolInformationType defined in the CybOX Common data model).  For tools that are used in more than one analysis, there are two options: their definitions may be repeated in each Analysis field, or they may be defined once in one Analysis and then referenced in other Analyses by their ID.  We recommend the second approach to reduce duplication of data in a MAEC document.

If an Analysis involves a single tool, then the implicit assumption is that the tool specified in the Analysis is responsible for all the findings in the Bundle that it references. However, if multiple tools are defined for an Analysis, then each Action and Object associated with the Analysis should reference its relevant tool (already defined in an Analysis element) via its CybOX Discovery_Method field.  Note that a tool cannot be defined in line within an Action or Object.

### Default Vocabularies

MAEC defines its own maecVocabs:ActionObjectAssociationTypeVocab, which should be used instead of the default vocabulary defined in CybOX (cyboxVocabs:ActionObjectAssociationTypeVocab).

### Collections

If numerous Actions are captured in a Bundle, the Bundle Action_Collections field should be used if the Actions can be grouped according to type (e.g., “File Actions”).  Relationships between Behaviors and Actions can then be captured using the Action_Composition field inside of a Behavior.

Similarly, if numerous Objects are captured in a Bundle, the Bundle Object_Collections field should be used if Objects can be grouped according to type.  Relationships between Actions and Objects can then be captured using the Associated_Objects field inside of an Action.

### Extracted Features
Extracted features should be captured in an Object created within a MAEC Bundle.  For example, to capture the output of a packer detection tool (e.g., PEiD), one could create a  Bundle with a single Cyber Observables Expression (CybOX) Object field (inside the Bundle's Objects field of type ObjectListType) that uses the FileObjectType type from the CybOX File Object data model in its Properties field to capture the packer information. 

Note that when using this method, an entire CybOX Object field is created, which should not be mistakenly identified as a newly found file: it merely captures extracted features from the file already defined inside the Malware Instance Object Attributes field. To make this explicit, the content_type attribute of the Bundle should be set to 'extracted from subject.'
(Alternatively, although not recommended, extracted features can be defined inside of the existing File field that is contained in the Malware Instance Object Attributes field. If captured there, it would be redundant to capture the same information in a separate Object.)

