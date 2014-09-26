---
layout: flat
title: Suggested Practices
---

This page contains suggested practices (sometimes called best practices) for producing and consuming MAEC content. Following these practices will ensure the best conformance with the design goals of MAEC and the best compatibility with other MAEC tools. These are not requirements, however: in some cases, technical or business requirements will mean you can't comply with them and that's fine. Think of them as "do it this way unless you have a good reason not to".

## General Practices

General practices apply across MAEC (and sometimes CybOX).

## Formatting IDs

MAEC IDs are [XML QNames](http://en.wikipedia.org/wiki/QName). Each ID includes both a namespace portion (optional) and an ID portion (required) separated by a colon (:). The recommend approach to creating MAEC IDs is to define a producer namespace and namespace prefix, then use the form:

`[ns prefix]:[construct type]-[GUID]`

The "ns prefix" should be a namespace prefix bound to a namespace owned/controlled by the producer of the content.

Some examples:

    acme:package-ce431003-ad07-4c96-bd7a-a50a3196e2a0
    acme:indicator-bf8bc5d5-c7e6-46b0-8d22-7500fea77196
    acme:campaign-79090715-8d6a-46b7-943b-c0bb9e063788

In order to use this approach, you will need to define that namespace prefix in the head of your XML document:

```xml
<maec:MAEC_Package xmlns:acme="http://acme.example.com" ...
```

This format provides high assurance that IDs will be both unique and meaningful, because the producer namespace denotes who's producing it, the construct name denotes what it is, and the overall ID including the GUID lends a high degree of confidence in its uniqueness.

## Assigning IDs

MAEC has several constructs with the potential to assign IDs to them such that they can be unambiguously referenced from elsewhere.

Technically the decision to specify an ID on a given construct is optional based on the specifics of the usage context.

As a simple general rule specifying IDs on particular instances of constructs enables clear referencing, relating and pivoting.

This supports several very common MAEC use cases such as:

* enabling individual portions of content to be externally referenced unambiguously (e.g. a report talking about a specific Campaign or Threat Actor)
* enabling the sharing/resharing of portions of MAEC content (e.g. PartyB resharing 2 of a set of 100 Indicators received from PartyA)
* enabling versioning of content


For these reasons, it is suggested that IDs be specified for the following commonly referenced and/or reused constructs unless there is clear reason not to:

* [Package](/data-model/{{site.current_version}}/stix/STIXType)
* [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
* [TTP](/data-model/{{site.current_version}}/ttp/TTPType)
* [Threat_Actor](/data-model/{{site.current_version}}/ta/ThreatActorType)
* [Campaign](/data-model/{{site.current_version}}/campaign/CampaignType)
* [Exploit_Target](/data-model/{{site.current_version}}/et/ExploitTargetType)
* [Course_Of_Action](/data-model/{{site.current_version}}/coa/CourseOfActionType)
* [Observable](/data-model/{{site.current_version}}/cybox/ObservableType)
* [Object](/data-model/{{site.current_version}}/cybox/ObjectType)
* [Action](/data-model/{{site.current_version}}/cybox/ActionType)
* [Event](/data-model/{{site.current_version}}/cybox/EventType)

As a simple general rule specifying IDs is not suggested for constructs embedded within other constructs (e.g. a CybOX Object containing the embedded specification of another CybOX Related_Object) where the embedded constructs are really only relevant/valid/important within the context of the enclosing construct. In other words they provide contextual characterization for the enclosing construct but would not be of interest on their own. 
The upside of this is slightly less complexity of IDs on everything. The downside is that it would not be possible to reference or pivot on the embedded constructs.

