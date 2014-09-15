---
layout: flat
title: Data Model Documentation
---

<link href="/css/data_model.css" rel="stylesheet"/>


## Package
<section class="data-model-section">
The [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) enables a user to share MAEC characterized data for one or more Malware Subjects.
</section>
## Malware Subject
<section class="data-model-section">
A MAEC [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) contains details of a particular malware instance (e.g., a file as identified by MD5 and/or SHA1 hash), any minor variants of the same instance that may have been observed (e.g., the same file but with different names), along with all of the analyses that were performed on the instance, any findings generated from the analyses, and any other metadata.  As such, the Malware Subject is MAEC's representation of a malware instance and all of the known data associated with it.
</section>


## Bundle
<section class="data-model-section">
The [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/Bundle) serves as a container and transport mechanism for use in storing and subsequently sharing MAEC-encoded information about malware, which may include MAEC Actions, Behaviors, and Capabilities as well as other attributes obtained from the characterization of a malware instance. 

A MAEC Bundle is very flexible and can be used to describe anything from a particular malware persistence method (composed of several low-level Actions and mid-level Behaviors) to the process tree observed when the instance is executed.  A MAEC Bundle can also contain intelligence-derived indicators as well as other signatures and patterns useful in network and host-based intrusion detection.
</section>