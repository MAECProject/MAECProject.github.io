---
layout: flat
title: Data Model Documentation
---

<link href="/css/data_model.css" rel="stylesheet"/>


## Package
<section class="data-model-section">
The [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) permits for the capture of one or more Malware Subjects.
</section>
## Malware Subject
<section class="data-model-section">
A MAEC [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) contains details of a particular malware instance (e.g., a file as identified by MD5 and/or SHA1 hash), any minor variants of the same instance that may have been observed (e.g., the same file but with different names), along with all of the analyses that were performed on the instance, any findings generated from the analyses, and any other metadata.  As such, the Malware Subject is MAEC's representation of a malware instance and all of the known data associated with it.
</section>


## Bundle
<section class="data-model-section">
The [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) serves as a container and transport mechanism for use in storing and subsequently sharing MAEC-encoded information about malware, which may include MAEC Actions, Behaviors, and Capabilities as well as other attributes obtained from the characterization of a malware instance. 

A MAEC Bundle is very flexible and can be used to describe anything from a particular malware persistence method (composed of several low-level Actions and mid-level Behaviors) to the process tree observed when the instance is executed.  Also, a MAEC Bundle can contain intelligence-derived indicators as well as other signatures and patterns useful in network and host-based intrusion detection.

MAEC Bundles can be used in two manners:
1. As a component embedded in a Malware Subject, as a means of capturing the results of some particular analysis performed on the Malware Subject.
2. In a standalone capacity, as a means of capturing all of the known analysis-derived data for a particular malware instance. 
</section>
## Malware Action
<section class="data-model-section">
A[Malware Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType) is a CybOX entity extended by MAEC for capturing a system state change or a similar operation that represents the fundamental low-level operation of malware.  Some examples include the creation of a file, deletion of a registry key, and the sending of some data on a socket.
</section>
## Behavior
<section class="data-model-section">
A [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType) is a MAEC entity for capturing the intent behind the execution of a specific set of instructions (or API calls) by a malware instance. In this manner, a Behavior can be thought of as the context (i.e., the why?) behind one or more Actions (i.e., the what?). Example: the creating a registry key (Action) may allow a malware instance to become resident at system start-up (Behavior).
</section>
## Capability
<section class="data-model-section">
A [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType) is a high-level MAEC entity for capturing a particular goal of the author(s) of a malware instance and used to organize groups of Behaviors.  Example: ensuring that malware is executed at start-up is a Behavior that is typically part of a :"Persistence" Capability.  
</section>
## Object
<section class="data-model-section">
An [Object](/data-model/{{site.current_version}}/cybox/ObjectType) is a CybOX entity for capturing the characteristics of a specific cyber-relevant object, including its particular properties and relationships to other Objects.  Examples: file, registry key, or process (which are typically captured in MAEC using further defined object models). 
</section>
## Process Tree
<section class="data-model-section">
A [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) is a MAEC entity for capturing the the hierarchy of processes created, modified, or affected by the execution of the malware instance. The fields of a MAEC Process Tree include parent process information and spawned or injected process information, along with any initiated Actions.
</section>