---
layout: flat
title: Creating a MAEC Package
summary: This Idiom demonstrates how to capture basic information about a single malware instance using the MAEC Package, through the use of its Malware Subject entity.
---

This Idiom demonstrates how to capture information about a single malware instance using the MAEC Package, through the use of its Malware Subject entity. While we'll describe the basic process of creating a Package and Malware Subject here, this process is also applicable to the creation of more detailed content, such as for the capture of static or dynamic analysis results.


## Data model

<img src="maec_package.png" alt="Package and Malware Subject Overview" class="aside-text"/>

To begin, we create a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType).  A MAEC Package has two required attributes:

1.	*id*. The id field captures a globally unique identifier for the Package. The recommended form for MAEC identifier attributes is "maec-namespace-entity_type-unique_identifier" where the namespace is optional and specified by the producer.  It is recommended that the namespace be meaningful and that the identifier be a globally unique ID (GUID).  For example, the identifier "maec-anubis_to_maec-act-1" uses the namespace "anubis_to_maec" to specify that the Anubis to MAEC translator tool  was used to create the MAEC output.  It is also recommended that the same namespace be used throughout a Package, although this is not required.

2.	*schema_version*. The schema_version field specifies the version of the schema used to create the Package.

As indicated by the figure, a MAEC Package encompasses one or more [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectEntity) entities. A Malware Subject is MAEC's primary unit for capturing all known data about a malware instance, including metadata such as the various analyses that were performed on it, as well as the actual findings of those analyses. 

Next, let's create a basic [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType), for capturing the identity of some malware instance. This will require populating two fields:

1.	*id*. As with the Package, the id field is required and should follow the form "maec-namespace-entity_type-unique_identifier".

2.	*Malware_Instance_Object_Attributes*. The [Malware_Instance_Object_Attributes](/data-model/{{site.current_version}}/cybox/ObjectType) field captures the identity of the malware instance that the Malware Subject characterizes.  Its base type is the [CybOX ObjectType](/data-model/{{site.current_version}}/cybox/ObjectType), and therefore it has an extension point via its [Properties](/data-model/{{site.current_version}}/cyboxCommon/ObjectPropertiesType) field where the properties of one of the CybOX defined objects may be used. For the sake of an example, let's assume that the malware instance we're characterizing is a file with a name of badware.exe, size of 1024 bytes, and MD5 hash of B6C39FF68346DCC8B67AA060DEFE40C2. As such, we'd use the defined [CybOX File Object](/data-model/{{site.current_version}}/FileObj/FileObjectType) as the extension for the Properties field, and specifically its native "File_Name", "Size_In_Bytes", and "Hashes" fields to capture the known information about the identity of the malware instance. The first two fields are self explanatory, but the [Hashes](/data-model/{{site.current_version}}/cyboxCommon/HashListType) field is actually a list that encompass multiple hash values. Therefore, we'll populate it with a single [Hash](/data-model/{{site.current_version}}/cyboxCommon/HashType) entry, which contains child fields of "Type" and "Simple_Hash_Value". For "Type", which captures the type of cryptographic hash whose value we're capturing, we'll specify a value of "MD5"  from the default CybOX vocabulary that we'll use here, the [HashNameVocab-1.0](/data-model/{{site.current_version}}/cyboxVocabs/HashNameVocab-1.0). Accordingly, "Simple_Hash_Value" is exactly as it sounds, and will be used to capture the actual MD5 hash value.

This is but a small portion of what a MAEC Package and Malware Subject are able to capture. Please refer to the other Idioms for other, more detailed scenarios.
	
## XML

{% highlight xml linenos %}
<maecPackage:Malware_Subject id="example:malware_subject-36103092-46c5-4614-8096-142eebccc25b">
	<maecPackage:Malware_Instance_Object_Attributes id="example:object-034e3508-0b44-4614-9e70-ffc6c5c25ac1">
		<cybox:Properties xsi:type="FileObj:FileObjectType">
			<FileObj:File_Name>badware.exe</FileObj:File_Name>
			<FileObj:Size_In_Bytes>1024</FileObj:Size_In_Bytes>
			<FileObj:Hashes>
				<cyboxCommon:Hash>
					<cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">MD5</cyboxCommon:Type>
					<cyboxCommon:Simple_Hash_Value>B6C39FF68346DCC8B67AA060DEFE40C2</cyboxCommon:Simple_Hash_Value>
				</cyboxCommon:Hash>
			</FileObj:Hashes>
		</cybox:Properties>
	</maecPackage:Malware_Instance_Object_Attributes>
</maecPackage:Malware_Subject>
{% endhighlight %}

[Full XML](maec_basic_package.xml)
## Python

{% highlight python linenos %}
# Set up the necessary Package and Malware Subject, Analysis Bundle Instances
p = Package()
ms = MalwareSubject()

# Set the Malware_Instance_Object_Attributes on the Malware Subject
ms.malware_instance_object_attributes = Object()
ms.malware_instance_object_attributes.properties = File()
ms.malware_instance_object_attributes.properties.file_name = "badware.exe"
ms.malware_instance_object_attributes.properties.size_in_bytes = "1024"
ms.malware_instance_object_attributes.properties.add_hash("B6C39FF68346DCC8B67AA060DEFE40C2")

# Build up the full Package/Malware Subject hierarchy
p.add_malware_subject(ms)
{% endhighlight %}

[Full Python](maec_basic_package.py)
## Further Reading
* [Creating a MAEC Bundle] (../bundle_creation)
* [Capturing Dynamic Analysis Results] (../dynamic_analysis)
* [Capturing Static Analysis Results] (../dynamic_analysis)