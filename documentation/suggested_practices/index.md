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

### Properties Captured

The MAEC schema was developed to enable analysts to capture a full gamut of information about malware. However, a MAEC Bundle is valid with very little information: it is only necessary to define a unique identifier and to specify the MAEC schema version. All other fields in MAEC are optional; however it is recommended that the following fields be captured:

* Malware Instance Object Attributes field – used to provide the MAEC Bundle recipient with the information they require about the malware instance object. Note that this field is equivalent to the Malware Instance Object Attributes field that is contained inside of a Malware Subject in the MAEC Package, and is therefore only required if this MAEC Bundle is to be used in a stand-alone fashion.

* Malware Subject Relationship Information –Malware Subject relationship information should be provided for Packages that contain more than one Malware Subject. For example, Grouping_Relationship fields might be used to indicate that the one Package contains Eyestye variants and a second Package contains Zeus variants.

### Object References
Objects used in MAEC can be represented as embedded Objects (defined and nested inside of the entity that uses them) or as separate Objects (referenced from multiple Actions using the idref attribute).  The following recommendations are made:

* In cases where multiple Actions reference the same Object, the Object should be defined separately and referenced from each Action. For example, if one Action creates a file, and another Action reads from the same file, it is recommended that the file Object is created once and then referenced by both Actions rather than being defined twice. Aside from reducing file size, referencing separately defined Objects means that any changes or additions to the Objects’ content only need to be made in one location.

* An embedded Object should be used to define the Malware Subject in the Malware_Instance_Object_Attributes entity.

