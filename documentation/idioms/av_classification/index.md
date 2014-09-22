---
layout: flat
title: Capturing AV Classification Results
summary: This Idiom describes the process of capturing the classifications as reported by anti-virus (AV) tools when executed against a particular malware instance.
---

This Idiom describes the process of capturing the classifications as reported by anti-virus (AV) tools when executed against a particular malware instance. As with all analysis-derived results, those that come from AV tools can be captured through the use of a MAEC Bundle. However, such output will be captured exclusively through the use of the [AV Classification](/data-model/{{site.current_version}}/maecBundle/AVClassificationType) entity.

## Scenario

In this scenario, a malicious PE binary has been scanned with a number of anti-virus (AV) engines, which provide detection and associated classification information for the binary. For this example, we'll assume that the binary was scanned with engines from Microsoft, Symantec, and Trend Micro.

## Data model
As with many of the other Idioms, the first step is to create a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) with a [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) for capturing the information about the malware instance being analyzed. We should also add an [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity to the Malware Subject to capture some details relating the particular analysis that we're performing. The information on this process is not covered in this idiom, but can be found in the corresponding [Creating a MAEC Package](../package_creation) and [Capturing Analysis Metadata](../analysis_metadata) idioms.

Next, a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) is created. Once created, we must set the "content_type" attribute on the Bundle to define the type of content that it is characterizing.  In this case, since we're capturing the output of AV engines, we should set it to a value of "static analysis tool output" since most such engines statically analyze binaries to provide their classification. This is one of the values contained in the BundleContentTypeEnum enumeration used by this field. Finally, we should set the defined_subject attribute on the Bundle to a value of "false", since this Bundle will be contained in a Malware Subject, which has already defined the particular malware instance being characterized.

Now that we've set up the Bundle that will capture the AV tool classification output, we can begin to populate it with these results. To do so, we'll be using the [AV Classification](/data-model/{{site.current_version}}/maecBundle/AVClassificationType) entity, which is a MAEC extension of the [CybOX ToolInformationType](/data-model/{{site.current_version}}/cyboxCommon/ToolInformationType).  As such, the [AV Classification](/data-model/{{site.current_version}}/maecBundle/AVClassificationType) entity contains the following fields specifically relevant to the capture of such results:

1.	*Vendor*. The name of the AV tool vendor, e.g. Microsoft.

2.	*Version*. The version of the AV tool, if available.

3.	*Engine_Version*. The version of the AV engine used by the AV tool that assigned the classification to the malware instance. 

4.	*Definition_Version*. The version of the AV definitions used by the AV tool that assigned the classification to the malware instance.

5.	*Classification_Name*. The classification assigned to the malware instance object by the AV tool, if one was given. E.g., "Zbot.123". Note that if the AV tool does not detect or provide a classification for the malware instance, this field should not be included.

For the sake of simplicity in our example, let's assume that we only know the name of the vendor of each AV tool, along with the particular classification that it assigned to the PE binary (this assumes that each tool was able to detect the binary). Thus, we will create three instances of the the [AV Classification](/data-model/{{site.current_version}}/maecBundle/AVClassificationType) entity, one each for Microsoft, Symantec, and Trend Micro. In each such instance, we will use the "Vendor" field to capture the name of the tool vendor, and also the "Classification_Name" field to capture the actual classification that it gave to the PE binary.

After creating these [AV Classification](/data-model/{{site.current_version}}/maecBundle/AVClassificationType) instances, the remaining task is to add them to the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that was previously created. To do this, we simply need to use the [AV_Classifications](/data-model/{{site.current_version}}/maecBundle/AVClassificationsType) field at the root level of the Bundle, to which we'll add the three [AV Classification](/data-model/{{site.current_version}}/maecBundle/AVClassificationType) instances.

With the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) populated with the results of the AV tools, the final step is to add it to the Malware Subject. To do, we'll use the [Findings_Bundles](/data-model/{{site.current_version}}/maecPackage/FindingsBundleListType) field, and specifically will populate its child "Bundle" field with the Bundle that we've constructed.

## XML

{% highlight xml linenos %}
<maecPackage:Bundle defined_subject="false" id="example:bundle-c374ea27-8520-4ab7-9fba-3f18050d4e1c" schema_version="4.1" content_type="static analysis tool output">
	<maecBundle:AV_Classifications>
	 <maecBundle:AV_Classification>
	  <cyboxCommon:Name>Microsoft</cyboxCommon:Name>
	  <maecBundle:Classification_Name>PWS:Win32/Zbot.gen!B</maecBundle:Classification_Name>
	 </maecBundle:AV_Classification>
	 <maecBundle:AV_Classification>
	  <cyboxCommon:Name>Symantec</cyboxCommon:Name>
	  <maecBundle:Classification_Name>Backdoor.Paproxy</maecBundle:Classification_Name>
	 </maecBundle:AV_Classification>
	 <maecBundle:AV_Classification>
	  <cyboxCommon:Name>TrendMicro</cyboxCommon:Name>
	  <maecBundle:Classification_Name>TSPY_ZBOT.TD</maecBundle:Classification_Name>
	 </maecBundle:AV_Classification>
	</maecBundle:AV_Classifications>
</maecPackage:Bundle>
{% endhighlight %}

[Full XML](maec_av_classification.xml)
## Python

{% highlight python linenos %}
# Create the first, create file action
act1 = MalwareAction()
act1.name = "create file"
act1.name.xsi_type = "FileActionNameVocab-1.1"
act1.associated_objects = AssociatedObjects()
o1 = AssociatedObject()
o1.properties = WinExecutableFile()
o1.properties.file_name = "Zcxaxz.exe"
o1.properties.size_in_bytes = "332288"
o1.association_type = VocabString()
o1.association_type.value = "output"
o1.association_type.xsi_type = "maecVocabs:ActionObjectAssociationTypeVocab-1.0"
act1.associated_objects.append(o1)

# Create the second, create mutex action
act2 = MalwareAction()
act2.name = "create mutex"
act2.name.xsi_type = "SynchronizationActionNameVocab-1.0"
act2.associated_objects = AssociatedObjects()
o2 = AssociatedObject()
o2.properties = WinMutex()
o2.properties.name = "redem-Mutex"
o2.association_type = VocabString()
o2.association_type.value = "output"
o2.association_type.xsi_type = "maecVocabs:ActionObjectAssociationTypeVocab-1.0"
act2.associated_objects.append(o2)
{% endhighlight %}

[Full Python](maec_dynamic_analysis.py)

## Further Reading
* [Creating a MAEC Bundle] (../bundle_creation)
* [Creating a MAEC Package] (../package_creation)
* [Capturing Static Analysis Results] (../static_analysis)