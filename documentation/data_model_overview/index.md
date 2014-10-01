---
layout: flat
title: Overview of the MAEC Data Models
---
The MAEC Language is defined by three data models, each of which is implemented in its own XML schema.  There is also a default vocabularies schema, which defines a default set of controlled vocabularies used within MAEC.

<img src="datamodels.png" alt="MAEC data models" class="sm-aside-text" height="237" width="350"/>

As illustrated, “MAEC Bundle” is the (lowest) Tier 1 data model; “MAEC Package” is the (middle) Tier 2 data model; and “MAEC Container” is the (highest) Tier 3 data model.  All three data models offer a stand-alone output format, so a lower level model can be used without the higher tier data model (although each model level requires all lower tiers).  This three-tiered structure provides flexibility in the type and amount of information that can be shared.  

<p></p>

<div class="row">
  <div class="col-md-6">
    <div class="well">
      <h4>MAEC Bundle Data Model</h4>
      <p>The MAEC Bundle data model provides the ability to capture and share data obtained from the analysis of a single malware instance.  </p>
	  <a class="btn btn-primary" href="bundle">MAEC Bundle »</a>
    </div>
  	<div class="well">
      <h4>MAEC Package Data Model</h4>
      <p>The MAEC Package data model enables a user to share MAEC characterized data for one or more Malware Subjects.</p>
      <a class="btn btn-primary" href="package">MAEC Package »</a>
    </div>
  </div>
  <div class="col-md-6">
  	<div class="well">
      <h4>MAEC Container Data Model</h4>
      <p>The MAEC Container data model enables a user to share any collection of MAEC characterized data.</p>
	  <a class="btn btn-primary" href="container">MAEC Container »</a>
    </div>
  </div>
</div>