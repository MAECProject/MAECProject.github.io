---
layout: flat
title: Capturing Analysis Metadata & Results
summary: This Idiom describes the process of capturing the metadata and results associated with a particular analysis performed on a malware instance. 
---

This Idiom describes the process of capturing the metadata and results associated with a particular analysis performed on a malware instance.  The capture of such metadata can provide useful context surrounding the methods use to analyze a malware instance, such as information on the tools used and their associated findings. As such, the focal point of this idiom revolves around the [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity.

## Scenario

In this scenario, a malicious PE binary has been analyzed with the PEiD static analysis tool, along with the Anubis sandbox, a dynamic analysis tool. Thus, we, the malware analyst, wish to capture the metadata about these analyses, along with their particular output. 

## Data model
As with many of the other Idioms, the first step is to create a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) with a [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) for capturing the information about the malware instance being analyzed. Please see the [Creating a MAEC Package] (../package_creation) idiom for more details on this process.

With the [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) created and populated with the identity of the malware instance that we're characterizing, we can now focus on adding the metadata on the analyses that were performed. For this, we'll use the [Analyses](/data-model/{{site.current_version}}/maecPackage/AnalysisListType), which is a list element that captures these analyses. 

Populating the [Analyses](/data-model/{{site.current_version}}/maecPackage/AnalysisListType) is the [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity, which is MAEC's mechanism for capturing details of an analysis that was performed on a malware instance. As with many of the other MAEC entities, the Analysis has a required field:

1.  *id*. The "id" field is intended to capture a globally unique identifier for the Analysis. The recommended form for MAEC identifier attributes is "maec-namespace-entity_type-unique_identifier" where the namespace is optional and specified by the producer.  It is recommended that the namespace be meaningful and that the identifier portion be a globally unique ID (GUID).  For example, the identifier "maec-anubis_to_maec-analysis-5cbf19d5-9067-4202-8424-b3676f51b606" uses the namespace "anubis_to_maec" to specify that the Anubis to MAEC translator tool  was used to create the MAEC output.  It is also recommended that the same namespace be used throughout a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType), although this is not required. 

Besides this required field, the [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) also contains a number of useful, optional fields. We won't go over all of them here, but there are a number that are commonly used and therefore worth pointing out:

1.	*type*. The type field specifies the type of malware analysis being performed, using values found in the AnalysisTypeEnum. Thus, the possible values are "triage" and "in-depth". When used together with the "method" field, it provides a simple way of specifying the nature of the analysis that was performed.

2.	*method*. The method field specifies the analysis method used in the analysis, using values found in the AnalysisMethodEnum. Thus, the possible values are "static", "dynamic", and "combination". When used together with the "type" field, it provides a simple way of specifying the nature of the analysis that was performed.

3.	*Summary*. The Summary field specifies a textual summary of the analysis that was performed. It should be high-level and concise. 

4.	*Findings_Bundle_Reference*. The [Findings_Bundle_Reference](/data-model/{{site.current_version}}/maecBundle/BundleReferenceType) field specifies a reference to the Bundle which encompasses the results and output of the Analysis in terms of its corresponding MAEC entities, such as Behaviors and Actions. More than one Bundle may be referenced by using multiple occurrences of this field.

5.	*Tools*. The [Tools](/data-model/{{site.current_version}}/maecPackage/ToolListType) field specifies information about the tool(s) used in the analysis, via the CybOX ToolInformationType. If only a single Tool is specified, then this implies that this tool was responsible for all of the findings contained in the Bundle referenced by the Findings_Bundle_Reference element. Tools used in an analysis are defined inline within the Analysis field rather than defined at a higher level and then referenced.  Consequently, it is valid to have the same tool be defined more than once within a Package.

Now that we've defined some of the most useful fields in the [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity, let's see how they would be used in our example scenario.

## Example
Since we performed two analyses on our malware instance, one with PEiD, and one with Anubis, we need to construct two corresponding [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entities. 

### PEiD Analysis

After creating the base [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) instance, we'll want to capture a few useful aspects regarding the analysis performed by PEiD: 

1.	The type of analysis performed, via the "type" field in the Analysis. Since PEiD is an automated tool that doesn't typically correspond to in-depth manual analysis, we'll want to use the value of "triage" for this field from the corresponding AnalysisTypeEnum.

2.	The particular analysis method that was used, via the "method" field in the Analysis. Since PEiD is a static analysis tool, as it does not execute the subject binary, we'll want to use the value of "static" for this field from the corresponding AnalysisMethodEnum.

3.	The information about the tool(s) used, via the "Tools" field in the Analysis. Since the "Tools" field is a list type that encompasses one or more [Tool](/data-model/{{site.current_version}}/cyboxCommon/ToolInformationType) fields, we'll want to create a single [Tool](/data-model/{{site.current_version}}/cyboxCommon/ToolInformationType) entry to capture the information about the PEiD tool. Inside this entry, we'll use the "Name" and "Version" fields to capture the name of the tool and its version, respectively.

4.	The actual output of the tool as characterized in MAEC, via the "Findings_Bundle_Reference" field, which references the particular [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that contains this output. The details of this process can be found in the [Capturing Static Analysis Results] (../static_analysis) idiom.

### Anubis Analysis

After creating the base [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) instance, we'll similarly want to capture a few useful aspects regarding the analysis performed by Anubis: 

1.	The type of analysis performed, via the "type" field in the Analysis. Since Anubis is an automated tool that doesn't typically correspond to in-depth manual analysis, we'll want to use the value of "triage" for this field from the corresponding AnalysisTypeEnum.

2.	The particular analysis method that was used, via the "method" field in the Analysis. Since Anubis is a dynamic analysis tool, which executes the subject binary, we'll want to use the value of "static" for this field from the corresponding AnalysisMethodEnum.

3.	The information about the tool(s) used, via the "Tools" field in the Analysis. Since the "Tools" field is a list type that encompasses one or more [Tool](/data-model/{{site.current_version}}/cyboxCommon/ToolInformationType) fields, we'll want to create a single [Tool](/data-model/{{site.current_version}}/cyboxCommon/ToolInformationType) entry to capture the information about the PEiD tool. Inside this entry, we'll use the "Name" and "Version" fields to capture the name of the tool and its version, respectively.

4.	The actual output of the tool as characterized in MAEC, via the "Findings_Bundle_Reference" field, which references the particular [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that contains this output. The details of this process can be found in the [Capturing Dynamic Analysis Results] (../dynamic_analysis) idiom.

## XML

{% highlight xml linenos %}
<maecPackage:Analysis id="example:analysis-181c7d30-9f22-42f3-996a-ebfde66eeed6" method="static" type="triage">
	<maecPackage:Tools>
		<maecPackage:Tool id="example:tool-49fd2bca-7631-4619-ba9f-2ab32b819122">
			<cyboxCommon:Name>PEiD</cyboxCommon:Name>
			<cyboxCommon:Version>0.94</cyboxCommon:Version>
		</maecPackage:Tool>
	</maecPackage:Tools>
</maecPackage:Analysis>
<maecPackage:Analysis id="example:analysis-f30ce041-ee2f-410d-9c14-2418d6e475aa" method="dynamic" type="triage">
	<maecPackage:Tools>
		<maecPackage:Tool id="example:tool-7882ca14-39ac-43c0-b2b0-086a24d36c2a">
			<cyboxCommon:Name>Anubis</cyboxCommon:Name>
			<cyboxCommon:Vendor>1.68.0</cyboxCommon:Vendor>
		</maecPackage:Tool>
	</maecPackage:Tools>
</maecPackage:Analysis>
{% endhighlight %}

[Full XML](maec_analysis_metadata.xml)
## Python

{% highlight python linenos %}
# Populate the PeID Analysis with its corresponding metadata
a1.method = "static"
a1.type_ = "triage"
t1 = ToolInformation()
t1.name = "PEiD"
t1.version = "0.94"
a1.add_tool(t1)

# Populate the Anubis Analysis with its corresponding metadata
a2.method = "dynamic"
a2.type_ = "triage"
t2 = ToolInformation()
t2.name = "Anubis"
t2.version = "1.68.0"
a2.add_tool(t2)
{% endhighlight %}

[Full Python](maec_analysis_metadata.py)

## Further Reading
* [Creating a MAEC Bundle] (../bundle_creation)
* [Creating a MAEC Package] (../package_creation)
* [Capturing Static Analysis Results] (../static_analysis)
* [Capturing Dynamic Analysis Results] (../dynamic_analysis)
