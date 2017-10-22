---
layout: flat
title: MAEC Language Versioning Policy
---


This document details the current methodology for determining whether a revision will require a major version change, a minor version change, or an update version change as well as how version information is represented and conveyed in the [MAEC Language](/releases/5.0/).

### MAEC Language Versioning

A three-component version identifier is used to track the evolution of the MAEC Language over time. Each component of the version identifier is a numeric value and corresponds to one of the three release types — "Major," "Minor," and "Update" — where the complete version identifier has the following form: MAJOR.MINOR.UPDATE (e.g., "5.0.1").           

A high-level overview of each type of MAEC release is described below:          

* **Major Release** — A major release adds features that require breaking backward compatibility with previous versions of the MAEC Language or represent fundamental changes to concepts in the MAEC Language. For a major release, the MAJOR component is incremented by one and the MINOR and UPDATE components are set to zero.          

* **Minor Release** — A minor release adds features that do not break backward compatibility with previous versions and for fixing bugs that may or may not break backwards compatibility. For a minor release, the MINOR component is incremented by one and the UPDATE component is set to zero.          

* **Update Release** — An update release may only be initiated to address critical defects that affect usability. Fixes may break backward compatibility if necessary. New functionality outside of what was intended in the previous MAJOR.MINOR release is not permitted. However, once an update release is agreed to, other non-critical fixes and clarifications may be addressed. When an update version change is made, the UPDATE component is incremented by one.          

Each of the MAEC schemas are versioned similarly to the MAEC Language. Details are provided in the [MAEC Language Specification](/releases/5.0/#specifications).
