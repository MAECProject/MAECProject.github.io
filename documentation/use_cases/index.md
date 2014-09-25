---
layout: flat
title: MAEC Use Cases
---

At its highest level, MAEC is a domain-specific language for non-signature based malware characterization.  Because MAEC provides a common vocabulary and grammar for the malware domain, it follows that the majority of the use cases for MAEC are motivated by the unambiguous and accurate communication of malware attributes enabled by MAEC.  We provide high level use cases in the following four general areas.  

<div class="row">
  <div class="col-md-6">
    <div class="well">
      <h4><a href="malware_analysis">Malware Analysis</a></h4>
      <p>This set of Use Cases demonstrate how MAEC be used to encode the data obtained from malware analysis.  In such a scenario, a malware instance is analyzed automatically or manually using either dynamic or static methods.  The results are then captured using the MAEC schema and either a single MAEC Package (with one or more MAEC Bundles) or one or more standalone MAEC Bundles are generated to communicate the analysis results.  As is also discussed, MAEC Packages and MAEC Bundles can also be used to help with visualization, to capture data for storage in analysis-oriented repositories, and as a means for standardizing tool output.</p>
      <a class="btn btn-primary" href="malware_analysis">Go »</a>
    </div>
	<div class="well">
      <h4><a href="cyber_threat_analysis">Cyber Threat Analysis</a></h4>
      <p>This set of Use Cases demonstrates how capturing cyber threat analysis information in MAEC will result in a threat being more readily understood and evaluated because the information will be more consistent across analysts and incidents.  In addition, we show how MAEC's standardized encoding of the Capabilities exhibited by a malware instance will allow for the accurate discernment of the threat that the malware poses to an organization and its infrastructureMAEC is used to visualize malware.</p>
      <a class="btn btn-primary" href="cyber_threat_analysis">Go »</a>
    </div>
	<div class="well">
      <h4><a href="intrusion_detection">Intrusion Detection</a></h4>
      <p>This Use Case demonstrates how using MAEC to characterize malware based on its attributes provides actionable information for malware intrusion detection and assessment.</p>
      <a class="btn btn-primary" href="intrusion_detection">Go »</a>
    </div>
  </div>
  <div class="col-md-6">
    <div class="well">
      <h4><a href="incident_management">Incident Management</a></h4>
      <p>This set of Use Cases describes how a uniform malware reporting format, standardized malware repositories, and the ability to verify remediation procedures - all based on the MAEC data model - greatly enhance malware-related incident management efforts.</p>
      <a class="btn btn-primary" href="standardized_tool_output">Go »</a>
    </div>
  </div>
</div>