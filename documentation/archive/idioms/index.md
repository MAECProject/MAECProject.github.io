---
layout: flat
title: Suggested Practices for MAEC Version 4.1
---

This page contains suggested practices (sometimes called best practices) for producing and consuming MAEC content. Following these practices will ensure the best conformance with the design goals of MAEC and the best compatibility with other MAEC tools. These are not requirements, however: in some cases, technical or business requirements will mean you can't comply with them and that's fine. Think of them as "do it this way unless you have a good reason not to."

## General Practices

General practices apply across MAEC.

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

* [Package](/documentation/data-model/{{site.current_version}}/maecPackage/PackageType)
* [Malware Subject](/documentation/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType)
* [Analysis](/documentation/data-model/{{site.current_version}}/maecPackage/AnalysisType)
* [Bundle](/documentation/data-model/{{site.current_version}}/maecBundle/BundleType)
* [Capability](/documentation/data-model/{{site.current_version}}/maecBundle/CapabilityType)
* [Process Tree Node](/documentation/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType)
* [Behavior](/documentation/data-model/{{site.current_version}}/maecBundle/BehaviorType)
* [Candidate Indicator](/documentation/data-model/{{site.current_version}}/maecBundle/CandidateIndicatorType)
* [Behavior Collection](/documentation/data-model/{{site.current_version}}/maecBundle/BehaviorCollectionType)
* [Action Collection](/documentation/data-model/{{site.current_version}}/maecBundle/ActionCollectionType)
* [Object Collection](/documentation/data-model/{{site.current_version}}/maecBundle/ObjectCollectionType)
* [Candidate Indicator Collection](/documentation/data-model/{{site.current_version}}/maecBundle/CandidateIndicatorCollectionType)

Accordingly, MAEC extends or makes direct use of a number of [Cyber Observable eXpression (CybOX™)](https://cyboxproject.github.io/) entities. In these entities, the assignment of IDs is not required as in MAEC; however, we highly recommend assigning IDs for these constructs, for consistency with the MAEC-defined constructs and also potential re-use and referencing:

* [Malware Action](/documentation/data-model/{{site.current_version}}/maecBundle/MalwareActionType)
* [CybOX Object](/documentation/data-model/{{site.current_version}}/cybox/ObjectType)

### Recommended Properties

The MAEC schema was developed to enable analysts to capture a full gamut of information about malware. However, a [MAEC Bundle](/documentation/data_model_overview/bundle/) or [MAEC Package](/documentation/data_model_overview/package/) is valid with very little information: it is only necessary to define a unique identifier and to specify the MAEC schema version. While all other properties in MAEC are optional, it is recommended that the following fields are captured:

* Malware Instance Object Attributes field - this field should be used to provide the MAEC Bundle or Package recipient with the information they require about the malware instance object. Note that the Malware Instance Object Attributes field is defined both in the Bundle (BundleType) and in the Malware Subject of a Package (MalwareSubjectType).  The definitions are equivalent; however, the BundleType's Malware Instance Object Attributes field should only be used if the Bundle is used in a stand-alone fashion.  Otherwise, only the Package MalwareSubjectType's Malware Instance Object Attributes field should be used (note that when a Bundle is embedded in a Package, the defined_subject field of the Bundle must be set to `false`).

* Grouping Relationships field - Malware Subject relationship information should be provided for Packages that contain more than one Malware Subject. For example, the Grouping Relationships field might be used to indicate that the a Package contains several Zeus variants.

### Object References
Objects used in MAEC can be represented as embedded Objects (defined and nested inside of the fields that uses them) or as separate Objects (referenced from the places they are used with the *idref* attribute).  The following recommendations are made:

* In cases where multiple Actions reference the same Object, the Object should be defined separately and referenced from each Action. For example, if one Action creates a file, and another Action reads from the same file, it is recommended that the file Object is created once and then referenced by both Actions rather than being defined twice. Aside from reducing MAEC document size, referencing separately defined Objects means that any changes or additions to the Objects' content only need to be made in one location.

* An embedded Object should be used to define the Malware Subject in the Malware_Instance_Object_Attributes field.

### Tool References

Typically, tool information should be defined inline within an Analysis using the Tool field (of [ToolInformationType](/documentation/data-model/{{site.current_version}}/cyboxCommon/ToolInformationType) defined in the CybOX Common data model).  For tools that are used in more than one analysis, there are two options: their definitions may be repeated in each Analysis field, or they may be defined once in one Analysis and then referenced in other Analyses by their ID.  We recommend the second approach to reduce duplication of data in a MAEC document.

If an Analysis involves a single tool, then the implicit assumption is that the tool specified in the Analysis is responsible for all the findings in the Bundle that it references. However, if multiple tools are defined for an Analysis, then each Action and Object associated with the Analysis should reference its relevant tool (already defined in an Analysis element) via its CybOX Discovery_Method field.  Note that a tool cannot be defined inline within an Action or Object.

### Default Vocabularies

MAEC defines its own set of default vocabularies for certain entities, and these vocabularies should be should be used in place of any contextually similar vocabularies defined in CybOX. For example, the *maecVocabs:ActionObjectAssociationTypeVocab* should be used instead of the *cyboxVocabs:ActionObjectAssociationTypeVocab*.

### Collections

[Collections](/documentation/data-model/{{site.current_version}}/maecBundle/CollectionsType) in a [MAEC Bundle](/documentation/data-model/{{site.current_version}}/maecBundle/BundleType) can be used to organize groups of MAEC-defined entities around some particular context. For example, if multiple [Actions](/documentation/data-model/{{site.current_version}}/maecBundle/MalwareActionType) are captured in a Bundle, the Bundle [Action_Collections](/documentation/data-model/{{site.current_version}}/maecBundle/ActionCollectionListType) field could be used to group the Actions according to their type (e.g., “File Actions”). Similarly, if numerous [Objects](/documentation/data-model/{{site.current_version}}/cybox/ObjectType) are captured in a Bundle, the Bundle [Object_Collections](/documentation/data-model/{{site.current_version}}/maecBundle/ObjectCollectionListType) field can be used to group the Objects according to type.  

### Extracted Features
Features extracted from binaries should be captured in an Object created within a [MAEC Bundle](/documentation/data-model/{{site.current_version}}/maecBundle/BundleType).  For example, to capture the output of a packer detection tool (e.g., PEiD), one could create a Bundle with a single [CybOX Object](/documentation/data-model/{{site.current_version}}/cybox/ObjectType) inside of the Bundle's [Objects](/documentation/data-model/{{site.current_version}}/maecBundle/ObjectListType) field that uses the [Cybox File Object](/documentation/data-model/{{site.current_version}}/FileObj/FileObjectType) in its Properties extension field (by setting the *xsi:type* attribute) to capture the packer information. 

Note that when using this method, a separate [CybOX Object](/documentation/data-model/{{site.current_version}}/cybox/ObjectType) is created, which should not be mistakenly identified as a newly found file: it merely captures extracted features from the file already defined inside the Malware Instance Object Attributes field. To make this explicit, the content_type attribute of the Bundle that contains this Object should be set to `extracted from subject`.
