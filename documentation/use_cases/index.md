---
layout: flat
title: MAEC Use Cases
---

At its highest level, MAEC is a domain-specific language for non-signature based malware characterization.  Because MAEC provides a common vocabulary and grammar for the malware domain, it follows that the majority of the use cases for MAEC are motivated by the unambiguous and accurate communication of malware attributes enabled by MAEC.  

<div class="row">
  <div class="col-md-6">
    <div class="well">
      <h4>Malware Analysis</h4>
      <p>Malware analysis-related use cases demonstrate how MAEC can be used to effectively capture the data obtained from malware analysis.  As we illustrate in the first use case, a malware instance is analyzed automatically or manually using either dynamic or static methods.  The results are then captured using the MAEC schema and either a single MAEC Package (with one or more MAEC Bundles) or one or more standalone MAEC Bundles.  </p>
	  ▪ <a class="btn btn-primary" href="malware_analysis/static_dynamic_malware_analysis">Static and Dynamic Malware Analysis »</a>
	  <p></p>
	  <p>MAEC Packages and MAEC Bundles can also be used to help with visualization, to capture data for storage in analysis-oriented repositories, and as a means for standardizing tool output.</p>
      ▪ <a class="btn btn-primary" href="malware_analysis/malware_visualization">Malware Visualization »</a>
	  <p></p>
	  ▪ <a class="btn btn-primary" href="malware_analysis/analysis_oriented_malware_repositories">Analysis Oriented Malware Repositories »</a>
	  <p></p>
	  ▪ <a class="btn btn-primary" href="malware_analysis/standardized_tool_output">Standardized Tool Output »</a>
    </div>
  	<div class="well">
      <h4>Intrusion Detection</h4>
      <p>The intrusion detection use case demonstrates how MAEC can be used to characterize malware based on its attributes to provide actionable information for malware intrusion detection and assessment.</p>
      ▪ <a class="btn btn-primary" href="intrusion_detection">Intrusion Detection »</a>
    </div>
  </div>
  <div class="col-md-6">
  	<div class="well">
      <h4>Cyber Threat Analysis</h4>
      <p>Cyber threat analysis-related use cases demonstrate how capturing cyber threat analysis information in MAEC will result in a threat being more readily understood and evaluated because the information will be more consistent across analysts and incidents.  Furthermore, MAEC's standardized encoding of the Capabilities exhibited by a malware instance will allow for the accurate discernment of the threat that the malware poses to an organization and its infrastructure.</p>
	  ▪ <a class="btn btn-primary" href="cyber_threat_analysis/attribution">Attribution »</a>
	  <p></p>
      ▪ <a class="btn btn-primary" href="cyber_threat_analysis/malware_threat_scoring_system">Malware Threat Scoring System »</a>
    </div>
    <div class="well">
      <h4>Incident Management</h4>
      <p>Incident management-related use cases describe how a uniform malware reporting format, standardized malware repositories, and the ability to verify remediation procedures - all based on the MAEC data model - greatly enhance malware-related incident management efforts.</p>
      ▪ <a class="btn btn-primary" href="incident_management/uniform_malware_reporting_format">Uniform Malware Reporting Format »</a>
	  <p></p>
	  ▪ <a class="btn btn-primary" href="incident_management/malware_repositories">Malware Repositories »</a>
	  <p></p>
	  ▪ <a class="btn btn-primary" href="incident_management/remediation">Remediation »</a>
    </div>
  </div>
</div>