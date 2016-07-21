---
layout: flat
title: About MAEC
---

Malware Attribute Enumeration and Characterization (MAEC™) is a standardized language for sharing structured information about malware based upon attributes such as behaviors, artifacts, and attack patterns.

The goal of the MAEC (pronounced "mike") effort is to provide a basis for transforming malware research and response. MAEC aims to eliminate the ambiguity and inaccuracy that currently exists in malware descriptions and to reduce reliance on signatures. In this way, MAEC seeks to improve human-to-human, human-to-tool, tool-to-tool, and tool-to-human communication about malware; reduce potential duplication of malware analysis efforts by researchers; and allow for the faster development of countermeasures by enabling the ability to leverage responses to previously observed malware instances. The MAEC Language enables correlation, integration, and automation.

## Malware

Malicious software — also called "malware" — has existed in one form or another since the advent of the first PC virus in 1971. It is presently responsible for a host of malicious activities, ranging from the vast majority of spam email distribution through botnets to the theft of sensitive information via targeted social engineering attacks. Whether the attackers are script kiddies, "hacktivists," criminals, or nation states, all may use malware of some variety to negatively impact or gain access to an organization's network and infrastructure. Effectively an autonomous agent operating on behalf of the attacker, malware has the ability to perform any action capable of being expressed in code, and as such represents a prodigious threat to cyber security.

The protection of computer systems from malware is therefore currently one of the most important information security concerns for organizations and individuals, because even a single instance of uncaught malware can result in damaged systems and compromised data. Being disconnected from a computer network does not completely mitigate this risk of infection, as exemplified by malware that makes use of USB as its insertion vector. As such, the main focus of the majority of anti-malware efforts to date has been on preventing damaging effects through early detection.

There are currently several common methods utilized for malware detection, based mainly on physical signatures and heuristics. These methods are effective in terms of their narrow scope, although they have their own individual drawbacks, such as the fact that signatures are unsuitable for dealing with zero-day, targeted, polymorphic, and other forms of emerging malware. Similarly, heuristic detection may be able to generically detect certain types of malware while missing those for which it does not have patterns, such as kernel-level rootkits. Therefore, it would be safe to say that these methods, while still useful, cannot be exclusively relied upon to deal with the current influx of malware.

## Why MAEC

### Problem

Modern methods for detecting and combating malware often rely on the characterization of malware attributes and behaviors. Typically, such behaviors and attributes are discovered through the use of static and dynamic analysis techniques. The combination of the two allows for an encompassing profile of malware to be constructed based upon its disassembled binary and observed run-time behavior. Yet, such techniques are hampered by the non-existence of a widely accepted standard for unambiguously characterizing malware.

The lack of such a standard means that there is no clear method for communicating the specific attributes detected in malware by the aforementioned analyses, nor for enumerating its fundamental makeup. Several major problems result from this, including non-interoperable and disparate malware reporting between organizations, disjointed or inaccurate malware attribution, the duplication of malware analysis efforts, increased difficulty in determining the severity of a malware threat, and a greater period of time between malware infection and detection/response, among others.

On this basis, it is clear that a standard for describing malware in terms of its attack patterns, artifacts, actions, and behaviors is needed to address such issues and allow for the clear communication of the information gained using static and dynamic analysis.

### Solution

MAEC solves these problems. The characterization of malware using abstract patterns offers a wide range of benefits over the usage of physical signatures. It allows for the accurate encoding of how malware operates and the specific actions that it performs. Such information can not only be used for malware detection but also for assessing the end-goal the malware is pursuing and the corresponding threat that it represents.

Focusing on the attributes and behaviors of malware facilitates detection and analysis of emerging, sophisticated malware threats that circumvent the traditional signature-based and heuristic approaches. Characterizing malware in a standard way supports collaboration across organizations and the identification of common behavior, functionality, and code bases across instances of malware.

## Benefits

The adoption of MAEC for encoding high-fidelity information about malware has major benefits for the community:

### Elimination of ambiguity and inaccuracy in malware descriptions

MAEC allows for a vastly improved level of human-to-human, human-to-tool, tool-to-tool, and tool-to-human communication about anti-malware related information. This will positively impact all major stakeholders, including producers and consumers of malware analysis and related malware data, as well as the end-users of tools for malware prevention and mitigation.

### Reduced duplication of malware analysis efforts

A common method of characterizing malware along with a corresponding standard for malware analysis reporting will allow researchers and analysts to easily determine whether or not a particular malware instance has already been analyzed.

### Improved general awareness of malware

An adopted standard for characterizing malware will allow for increased public awareness of malware threats and activity due to its widespread usage throughout the entire anti-malware data producer to consumer chain.

### Decreased overall response time to malware threats

The standard method of describing malware behavior provided by MAEC will allow for the faster development of countermeasures based upon those developed for previously observed malware instances.

## MAEC Community

MAEC is industry-endorsed by the many antivirus vendors, operating system vendors, software vendors, IT users, security services providers, and other members of the information security community that are currently participating in the MAEC effort on the [MAECProject GitHub Repositories](https://github.com/MAECProject/), MAEC Development Group on [Handshake](https://handshake.mitre.org/), and [MAEC Community Discussion List](/community#discussion-lists--archives).

### Take the Next Step

We encourage you to join the [MAEC Community](/community/) and help build this growing, open-source industry effort.