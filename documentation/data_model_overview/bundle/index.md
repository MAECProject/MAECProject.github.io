---
layout: flat
title: Overview of the MAEC Bundle Data Model
---

The MAEC Bundle data model provides the ability to capture and share data obtained from the analysis of a single malware instance.  In terms of its most elemental structure, the MAEC Bundle data model can be thought of as having three interconnected layers, as shown in the figure.  

<img src="overview.png" alt="MAEC Bundle data model" class="aside-text" height="312" width="550"/>

While the MAEC Bundle data model also includes other components, the Actions, Behaviors, and Capabilities are key pieces of its underlying structure, and so we discuss each in further detail below.  

<p></p>

## Low-Level Actions
At the lowest layer, MAEC Actions answer the question of “what” the malware instance does on a system or network, and thus they characterize hardware accesses, network activity, and system state changes performed by malware.  As such, MAEC Action entities describe attributes tied to the basic functionality and low-level operation of malware, including system state changes such as the insertion of a registry key or the creation of a file.  Therefore, likely sources of such data include static analysis, dynamic analysis of malware binaries through sandboxes, and host-based and network-based intrusion detection and prevention systems (IDPS).

Actions can describe a wide range of activities, although initially we have concentrated on defining those that can be achieved through low-level API calls.  By design, MAEC Actions are relatively devoid of any significant intention:  while they answer the question of “what” the malware does, they don’t answer the question of “why” the malware performed the actions in the first place. 

Actions are represented at both semantic and syntactic levels in order to abstract actions from their implementations. Such abstracted Actions allow for the construction of a more concise grammar and also facilitate correlation between malware instances that may do similar things at this level but with vastly different implementations (such as malware targeted at different platforms). On the other hand, the implementation of a particular action or action type may provide insight that can be valuable for correlation or even attribution.

## Mid-Level Behaviors
The more interesting structure of the MAEC Bundle data model begins at the middle layer, which we term Behaviors. Behaviors are aimed at organizing and defining the purpose behind low-level Actions, whether in groups or as singletons. Thus, Behaviors serve to describe “how” a malware instance operates at significant level of abstraction, and can therefore represent discrete components of malware functionality at a level that is useful for analysis, triage, and detection. 

For instance, the description of a registry entry created or modified by malware can be useful for establishing its presence on a system. However, it does not give any insight into why the malware created or manipulated the registry entry. Such a registry entry inserted or modified by a malware instance could be associated with different behaviors.  For example, the registry entry could be used to ensure that the malware gets executed when the system boots, or it could be used as a simple flag to indicate that the system has been infected.  As we will discuss in the next section, including the necessary components for characterizing such mid-level Behaviors in the MAEC Language allows for the accurate description of the possible high-level intent or goals (i.e., Capabilities) that are behind the low-level Actions being performed by malware.

## High-Level Capabilities
At the more conceptual and upper-most layer, MAEC defines Capabilities.  Similar to the relationship between Behaviors and Actions, Capabilities serve to organize groups of Behaviors, and therefore they offer a standard way of capturing the set of high-level abilities that a malware instance possesses.  However, the key difference between Behaviors and Capabilities is that while Behaviors are intended to describe “how” a malware instance operates, Capabilities are meant to state “what” it is capable of doing.  In this sense, a Behavior may serve to describe a particular implementation of a Capability in a malware instance.

For example, ensuring that a malware instance is executed at start-up (e.g., by creating a binary copy of the malware somewhere on the local hard disk and/or by creating a particular registry entry) is a Behavior that is typically part of a ‘Persistence’ Capability.  Other examples of Capabilities include ‘Propagation’, ‘Self-Defense’, and ‘Data Theft’.  Because there is a relatively low upper bound on the number of possible capability types, MAEC Capabilities can be useful in terms of understanding the functionality of malware at a very high level.

Once higher order classifications are made, we envision that the Capabilities taxonomy will have “views” intended for different target audiences. For example, forensic analysts may only be interested in looking at malware payload Capabilities and Behaviors, while a SOC analyst might want to view Capabilities and Behaviors related to command and control.
