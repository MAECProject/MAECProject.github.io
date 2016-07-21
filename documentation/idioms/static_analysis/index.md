---
layout: flat
title: Capturing Static Analysis Results
summary: This Idiom describes the process of capturing the results of static analysis performed on some malware instance, such as through the use of a PE file analysis tool. 
---

This Idiom describes the process of capturing the results of static analysis performed on some malware instance, such as through the use of a PE file analysis tool. As with all analysis-derived results, those that come from static analysis can be captured through the use of a MAEC Bundle. However, unlike most other analyses, the output of static analysis can be captured using a [CybOX Object](/data-model/{{site.current_version}}/cybox/Object).

## Scenario

In this scenario, a malicious PE binary has been analyzed with the freely available PEiD tool. This tool provides information about the entry point and subsystem defined in the PE headers of the file, as well as the version of the linker used in linking the code.

## Data model

The following are the important MAEC data model constructs used in this idiom:

1. [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType): the MAEC Bundle is the MAEC entity that captures the results of one or more analyses performed on a malware instance, including from static analysis.
2. [CybOX Object](/data-model/{{site.current_version}}/cybox/ObjectType): the Object entity, defined in CybOX, can capture the properties of a single cyber-relevant object, such as a file, process, registry key, etc.

## Process

As with many of the other Idioms, the first step is to create a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) with a [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) for capturing the information about the malware instance being analyzed. We should also add an [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity to the Malware Subject to capture some details relating the particular analysis that we're performing. The information on this process is not covered in this idiom, but can be found in the corresponding [Creating a MAEC Package](../package_creation) and [Capturing Analysis Metadata](../analysis_metadata) idioms.

Next, a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) is created. Once created, we must set the *content_type* attribute on the Bundle to define the type of content that it is characterizing.  In this case, since we're capturing the output of a static analysis tool, we should set it to a value of `static analysis tool output`. This is one of the values contained in the BundleContentTypeEnum enumeration used by this field. Finally, we should set the *defined_subject* attribute on the Bundle to a value of `false`, since this Bundle will be contained in a Malware Subject, where we have already defined the identity of the particular malware instance being characterized.

<img src="static_analysis.png" alt="Capturing Static Analysis Results in a Bundle" class="aside-text"/>

Now that we've set up the Bundle that will capture the static analysis results, we can begin to populate it with these results. As depicted in the figure, we will use a [CybOX Object](/data-model/{{site.current_version}}/cybox/ObjectType) to capture the output of the static analysis tool that has extracted some features of the PE file that we're analyzing. 

Since we're dealing with a PE file in our example scenario, we should use the defined [CybOX Windows Executable Object](/data-model/{{site.current_version}}/WinExecutableFileObj/WindowsExecutableFileObjectType) to populate the *Properties* extension point of the CybOX Object. Other scenarios where different types of files are statically analyzed would require the use of the proper corresponding CybOX defined Object for the capture of their output; e.g., if we were statically analyzing a PDF File, we would use the [CybOX PDF File Object](/data-model/{{site.current_version}}/PDFFileObj/PDFFileObjectType).

Now that we've set up the proper CybOX Object/Properties hierarchy for the type of data that we're capturing, we can begin capturing the individual data points. As we mentioned before, we'll be capturing the entrypoint of the file, as well as the subsystem information and linker version. Since these are all properties stored in the headers of a PE File, we'll use the [Headers](/data-model/{{site.current_version}}/WinExecutableFileObj/PEHeadersType) field as the root for the capture of this data. Furthermore, since these properties are all part of the PE Optional Header, we'll use the corresponding [Optional Header](/data-model/{{site.current_version}}/WinExecutableFileObj/PEOptionalHeaderType) field in the Headers field to capture them. Specifically, we'll use the *Major_Linker_Version* and *Minor_Linker_Version* fields for the linker version, the *Subsystem* field for the subsystem information, and the *Address_Of_Entry_Point* field for the entry point information.

With the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) populated with the results of the static analysis, the final step is to add it to the Malware Subject. To do, we'll use the [Findings_Bundles](/data-model/{{site.current_version}}/maecPackage/FindingsBundleListType) field, and specifically will populate its child *Bundle* field with the Bundle that we've constructed.

## XML

{% highlight xml linenos %}
<maecPackage:Bundle id="example:bundle-704fd16d-486b-4797-b84c-167e1401c7c4" schema_version="4.1" defined_subject="false" content_type="static analysis tool output">
  <maecBundle:Objects>
    <maecBundle:Object id="example:object-0ad05b6d-3971-463d-80e2-dfa2d607d6d9">
      <cybox:Properties xsi:type="WinExecFileObj:WindowsExecutableFileObjectType">
        <WinExecFileObj:Headers>
          <WinExecFileObj:Optional_Header>
            <WinExecFileObj:Major_Linker_Version>06</WinExecFileObj:Major_Linker_Version>
            <WinExecFileObj:Minor_Linker_Version>00</WinExecFileObj:Minor_Linker_Version>
            <WinExecFileObj:Address_Of_Entry_Point>036418</WinExecFileObj:Address_Of_Entry_Point>
            <WinExecFileObj:Subsystem>Windows_GUI</WinExecFileObj:Subsystem>
          </WinExecFileObj:Optional_Header>
        </WinExecFileObj:Headers>
      </cybox:Properties>
    </maecBundle:Object>
  </maecBundle:Objects>
</maecPackage:Bundle>
{% endhighlight %}

[Full XML](maec_static_analysis.xml)

## Python

{% highlight python linenos %}
b.defined_subject = False
b.content_type = "static analysis tool output"
o = Object()
o.properties = WinExecutableFile()
o.properties.headers = PEHeaders()
o.properties.headers.optional_header = PEOptionalHeader()
o.properties.headers.optional_header.major_linker_version = "06"
o.properties.headers.optional_header.minor_linker_version = "00"
o.properties.headers.optional_header.address_of_entry_point = "036418"
o.properties.headers.optional_header.subsystem = "Windows_GUI"
{% endhighlight %}

[Full Python](maec_static_analysis.py)

## Further Reading
* [Creating a MAEC Bundle](../bundle_creation)
* [Creating a MAEC Package](../package_creation)
* [Capturing Dynamic Analysis Results](../dynamic_analysis)
