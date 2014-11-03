---
layout: flat
title: Common Features
---

This page contains an alphabetized list commonly characterized features - whether statically, dynamically, or manually identified in malware - along with their mappings to MAEC/CybOX object elements, the associated MAEC/CybOX schemas, the typical MAEC schema locations of the object elements (specified via a quasi-XPath like expression), and an explicit XML representation example. Note that all object elements are characterized through their Properties field, and that only the most commonly used object elements are listed for each feature (please refer to the applicable schemas for the complete lists).  

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>AV Classifications</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> MAEC_Bundle/AV_Classifications/AV_Classification/Engine_Version
		<li> MAEC_Bundle/AV_Classifications/AV_Classification/Definition_Version
		<li> MAEC_Bundle/AV_Classifications/AV_Classification/Classification_Name
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/maecBundle/BundleType>MAEC:maecBundle</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>---</td>
	<td>---</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:AV_Classifications> 
  <maecBundle:AV_Classification> 
    <cyboxCommon:Name>AhnLab-V3</cyboxCommon:Name> 
	<maecBundle:Classification_Name>Win32/IRCBot.worm.variant</maecBundle:Classification_Name> 
  </maecBundle:AV_Classification> 
  <maecBundle:AV_Classification> 
    <cyboxCommon:Name>Kaspersky</cyboxCommon:Name> 
	<maecBundle:Classification_Name>Packed.Win32.Katusha.a</maecBundle:Classification_Name> 
  </maecBundle:AV_Classification>
<maecBundle:AV_Classifications>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Code Attributes</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> CodeObj/Purpose
		<li> CodeObj/Code_Language
		<li> CodeObj/Code_Segment
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/CodeObj/CodeObjectType/>CybOX::CodeObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object/Related_Objects/Related_Object</td>
	<td>Used to capture code attributes related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture a code attributes related to an Object associated with a malware instance.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<cybox:Related_Object id="maec-example-obj-7"> 
  <cybox:Properties xsi:type="CodeObj:CodeObjectType"> 
    <CodeObj:Purpose>Shellcode</CodeObj:Purpose> 
    <CodeObj:Code_Language>Assembly</CodeObj:Code_Language> 
    <CodeObj:Code_Segment_XOR><![CDATA[76277b43e787dd1f67ebb85ed101]></CodeObj:Code_Segment_XOR> 
  </cybox:Properties> 
</cybox:Related_Object>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>CVE Identifier</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> MAEC_Bundle/Behaviors/Behavior/Purpose/Vulnerability_Exploit/CVE
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/maecBundle/BundleType>MAEC::maecBundle</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>---</td>
	<td>---</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Behavior id="maec-example-bhv-1"> 
  <maecBundle:Purpose> 
    <maecBundle:Vulnerability_Exploit> 
	  <maecBundle:CVE cve_id="CVE-2010-0188"/> 
	</maecBundle:Vulnerability_Exploit>
  </maecBundle:Purpose> 
</maecBundle:Behavior>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>File Attributes</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> File/File_Name
		<li> File/File_Path
		<li> File/Size_In_Bytes
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/FileObj/FileObjectType/>CybOX::FileObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinFileObj/WindowsFileObjectType/>CybOX::WinFileObj</a>
		<li> <a href=http://maecproject.github.io/data-model/4.1/WinExecutableFileObj/WindowsExecutableFileObjectType/>CybOX::WinExecFileObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes</td>
	<td>Used to capture information about a single file associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes</td>
	 <td>Used to capture information about a single file associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture information about a single file related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture information about a single file related to an Object associated with a malware instance, including an Object that represents some extracted feature (e.g., strings).</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture information about a single file related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture information about a single file related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<cybox:Associated_Object id="maec-example-obj-2"> 
  <cybox:Properties xsi:type="WinExecFileObj:WindowsExecutableFileObjectType"> 
    <FileObj:File_Name>ws2help.PNF</FileObj:File_Name> 
    <FileObj:File_Path>C:\Documents and Settings\user\Local Settings\Application\Data</FileObj:Full_Path>
    <FileObj:Size_In_Bytes>196608</FileObj:Size_In_Bytes>
  </cybox:Properties>
</cybox:Associated_Object>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>File Attributes - Windows PE File Attributes</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> Windows_Executable_File/Headers
		<li> Windows_Executable_File/PE_Checksum
		<li> Windows_Executable_File/Build_Information
		<li> Windows_Executable_File/Type
	  </ul>
    </td>
    <td>
      <ul>
		<li> <a href=http://maecproject.github.io/data-model/4.1/WinExecutableFileObj/WindowsExecutableFileObjectType/>CybOX::WinExecFileObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes</td>
	<td>Used to capture information about a single Windows PE file associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes</td>
	 <td>Used to capture information about a single Windows PE file associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture information about a single Windows PE file related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture information about a single Windows PE file related to an Object associated with a malware instance, including an Object that represents some extracted feature (e.g., strings).</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture information about a single Windows PE file related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture information about a single Windows PE file related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Object id="maec-example-obj-1">
  <cybox:Properties xsi:type="WinExecFileObj:WindowsExecutableFileObjectType"> 
    <WinExecFileObj:Headers> 
	  <WinExecFileObj:Optional_Header> 
	    <WinExecFileObj:Major_Linker_Version>06</WinExecFileObj:Major_Linker_Version> 
		<WinExecFileObj:Minor_Linker_Version>00</WinExecFileObj:Minor_Linker_Version> 
		<WinExecFileObj:Base_Of_Code>036418</WinExecFileObj:Base_Of_Code> 
		<WinExecFileObj:Subsystem>Windows_GUI</WinExecFileObj:Subsystem> 
	  </WinExecFileObj:Optional_Header> 
	</WinExecFileObj:Headers> 
    <WinExecFileObj:Type>Executable</WinExecFileObj:Type> 
  </cybox:Properties> 
</maecBundle:Object>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Hash - Fuzzy Hash</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> File/Hashes/Hash/Type[xsi:type=”cyboxVocabs:HashNameVocab-1.0”]={hash name} (e.g., SSDEEP)
		<li> File/Hashes/Hash/Fuzzy_Hash_Value
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/FileObj/FileObjectType/>CybOX::FileObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinFileObj/WindowsFileObjectType/>CybOX::WinFileObj</a>
		<li> <a href=http://maecproject.github.io/data-model/4.1/WinExecutableFileObj/WindowsExecutableFileObjectType/>CybOX::WinExecFileObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes</td>
	<td>Used to capture fuzzy hash information associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes</td>
	 <td>Used to capture fuzzy hash information associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture fuzzy hash information related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture fuzzy hash information related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture fuzzy hash information related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture fuzzy hash information related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecPackage:Malware_Subject id="maec-example-sub-2">
  <maecPackage:Malware_Instance_Object_Attributes> 
    <cybox:Properties xsi:type="WinExecutableFileObj:WindowsExecutableFileObjectType"> 
	  <FileObj:Hashes> 
	    <cyboxCommon:Hash> 
		  <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">SSDEEP</cyboxCommon:Type> 
		  <cyboxCommon:Fuzzy_Hash_Value>768:McAQ8tPlH25e85Q2OiYpD08NvHmjJ97UfPMO47sekO:uN9M553OiiN/OJ9MM+e3</cyboxCommon:Fuzzy_Hash_Value> 
        </cyboxCommon:Hash> 
	  </FileObj:Hashes> 
	</cybox:Properties> 
  </maecPackage:Malware_Instance_Object_Attributes>
</maecPackage:Malware_Subject>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Hash - Simple Hash</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> File/Hashes/Hash/Type[xsi:type=”cyboxVocabs:HashNameVocab-1.0”]={hash name} (e.g., MD5)
		<li> File/Hashes/Hash/Simple_Hash_Value
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/FileObj/FileObjectType/>CybOX::FileObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinFileObj/WindowsFileObjectType/>CybOX::WinFileObj</a>
		<li> <a href=http://maecproject.github.io/data-model/4.1/WinExecutableFileObj/WindowsExecutableFileObjectType/>CybOX::WinExecFileObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes</td>
	<td>Used to capture simple hash information associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes</td>
	 <td>Used to capture simple hash information associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture simple hash information related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture simple hash information related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture simple hash information related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture simple hash information related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecPackage:Malware_Subject id="maec-example-sub-1">
  <maecPackage:Malware_Instance_Object_Attributes> 
    <cybox:Properties xsi:type="WinExecutableFileObj:WindowsExecutableFileObjectType"> 
	  <FileObj:Hashes> 
	    <cyboxCommon:Hash> 
		  <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">MD5</cyboxCommon:Type> 
		  <cyboxCommon:Simple_Hash_Value>32530b68d78e5bcbd73a138276f45490</cyboxCommon:Simple_Hash_Value> 
        </cyboxCommon:Hash> 
	  </FileObj:Hashes> 
	</cybox:Properties> 
  </maecPackage:Malware_Instance_Object_Attributes>
</maecPackage:Malware_Subject>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>HTTP Session</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> HTTP_Session/HTTP_Request_Response/HTTP_Client_Request/ HTTP_Request_Line/HTTP_Method
		<li> HTTP_Session/HTTP_Request_Response/HTTP_Client_Request/ HTTP_Request_Line/Value
		<li> HTTP_Session/HTTP_Request_Response/HTTP_Client_Request/ HTTP_Request_Line/Version
		<li> HTTP_Session/HTTP_Request_Response/HTTP_Client_Request/ HTTP_Message_Body/Message_Body
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/HTTPSessionObj/HTTPSessionObjectType/>CybOX::HTTPSessionObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture information about a single HTTP session related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture information about a single HTTP session related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture information about a single HTTP session related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture information about a single HTTP session related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<cybox:Associated_Object id="maec-example-obj-1"> 
  <cybox:Properties xsi:type="HTTPSessionObj:HTTPSessionObjectType"> 
    <HTTPSessionObj:HTTP_Request_Response> 
	  <HTTPSessionObj:HTTP_Client_Request> 
	    <HTTPSessionObj:HTTP_Request_Line> 
		<HTTPSessionObj:HTTP_Method datatype="string">POST</HTTPSessionObj:HTTP_Method> 
		<HTTPSessionObj:Value>http://www.dailyinfonews.net/reportdatas.php</HTTPSessionObj:Value> 
		<HTTPSessionObj:Version>HTTP/1.0</HTTPSessionObj:Version> </HTTPSessionObj:HTTP_Request_Line> 
	  </HTTPSessionObj:HTTP_Client_Request> 
	</HTTPSessionObj:HTTP_Request_Response>
  </cybox:Properties>
</cybox:Associated_Object>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Malware Family Name <font size="3">(as a CybOX Object custom property)</font></feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> Custom_Properties/Property
	  </ul>
    </td>
    <td>
      <ul>
		<li> <a href=http://maecproject.github.io/data-model/4.1/cybox/PropertiesType/>CybOX::cybox</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes/Properties</td>
	 <td>Used to capture a malware family name associated with a malware instance.</td>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Malware_Instance_Object_Attributes> 
  <cybox:Properties>
    <cybox:CustomProperties>
	  <cybox:Property name="Family Name" description="Zeus"/>
	</cybox:CustomProperties>
  </cybox:Properties>
</maecBundle:Malware_Instance_Object_Attributes >
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Malware Family Name <font size="3">(as a grouping relationship)</font></feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> MAEC_Package/Grouping_Relationship/Type[xsi:type=”maecVocabs:GroupingRelationshipTypeVocab-1.0”]=same malware family
		<li> MAEC_Package/Grouping_Relationships/Grouping_Relationship/ Malware_Family_Name
	  </ul>
    </td>
    <td>
      <ul>
		<li> <a href=http://maecproject.github.io/data-model/4.1/maecPackage/GroupingRelationshipType/>MAEC::maecPackage</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>--</td>
	 <td>--</td>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecPackage:Grouping_Relationships>
  <maecPackage:Grouping_Relationship>
    <maecPackage:Type xsi:type="maecVocabs:GroupingRelationshipTypeVocab-1.0">same malware family</maecPackage:Type>
	<maecPackage:Malware_Family_Name>Zeus</maecPackage:Malware_Family_Name>
  </maecPackage:Grouping_Relationship>
</maecPackage:Grouping_Relationships>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Mutex</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> Mutex/Name
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/MutexObj/MutexObjectType/>CybOX::MutexObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinMutexObj/WindowsMutexObjectType/>CybOX::WinMutexObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture the name of a single mutex related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture the name of a single mutex related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture the name of a single mutex related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture the name of a single mutex related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Action id="maec-example-act-3"> 
  <cybox:Name xsi:type="maecVocabs:SynchronizationActionNameVocab-1.0">create mutex</cybox:Name> 
  <cybox:Associated_Objects> 
    <cybox:Associated_Object id="maec-example-obj-3"> 
	  <cybox:Properties xsi:type="WinMutexObj:WindowsMutexObjectType" named="true"> 
	    <MutexObj:Name>redem-Mutex</MutexObj:Name> 
	  </cybox:Properties> 
	  <cybox:Association_Type xsi:type="maecVocabs:ActionObjectAssociationTypeVocab-1.0">output</cybox:Association_Type> 
	</cybox:Associated_Object> 
  </cybox:Associated_Objects> 
</maecBundle:Action>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Packer Information</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> File/Packer_List/Packer/Name
		<li> File/Packer_List/Packer/Version
		<li> File/Packer_List/Entry_Point
	  </ul>
    </td>
    <td>
      <ul>
		<li> <a href=http://maecproject.github.io/data-model/4.1/FileObj/FileObjectType/>CybOX::FileObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinFileObj/WindowsFileObjectType/>CybOX::WinFileObj</a>
		<li> <a href=http://maecproject.github.io/data-model/4.1/WinExecutableFileObj/WindowsExecutableFileObjectType/>CybOX::WinExecFileObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes</td>
	<td>Used to capture information about a single packer associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes</td>
	 <td>Used to capture information about a single packer associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture information about a single packer related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture information about a single packer related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   
    <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture information about a single packer related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture information about a single packer related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecPackage:Malware_Subject id="maec-example-sub-1"> 
  <maecPackage:Malware_Instance_Object_Attributes> 
    <cybox:Properties xsi:type="WinExecFileObj:WindowsExecutableFileObjectType"> 
	  <FileObj:Packer_List> 
	    <FileObj:Packer> 
		  <FileObj:Name>UPX</FileObj:Name> 
		  <FileObj:Signature>UPX v3.0.2</FileObj:Signature> 
		</FileObj:Packer> 
	  </FileObj:Packer_List> 
	</cybox:Properties>
  </maecPackage:Malware_Instance_Object_Attributes>
</maecPackage:Malware_Subject>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Process</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> Process/Name
		<li> Process/Image_Info/Path
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/ProcessObj/ProcessObjectType/>CybOX::ProcessObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinProcessObj/WindowsProcessObjectType/>CybOX::WinProcessObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture information about a single process related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture information about a single process related to an Object associated with a malware instance.</td>
  </tr>
    <tr>
	 <td>MAEC_Bundle/Process_Tree/Root_Process</td>
	 <td>Used to capture information about the root process of a process tree.</td>
  </tr> 
    <tr>
	 <td>MAEC_Bundle/Process_Tree/Root_Process/Injected_Process</td>
	 <td>Used to capture information about a single process that was injected by the root process of a process tree.</td>
  </tr>
    <tr>
	 <td>MAEC_Bundle/Process_Tree/Root_Process/Spawned_Process</td>
	 <td>Used to capture information about a single child process spawned by the root process of a process tree.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture information about a single process related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture information about a single process related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Action id="maec-example-act-4"> 
  <cybox:Name xsi:type="maecVocabs:ProcessMemoryActionNameVocab-1.0">allocate process virtual memory</cybox:Name> 
  <cybox:Associated_Objects> 
    <cybox:Associated_Object id="maec-example-obj-4"> 
	  <cybox:Properties xsi:type="WinProcessObj:WindowsProcessObjectType"> 
	    <ProcessObj:Name>services.exe</ProcessObj:Name> 
		<ProcessObj:Image_Info> 
		  <ProcessObj:Path>%System%\services.exe</ProcessObj:Path> 
		</ProcessObj:Image_Info> 
	  </cybox:Properties> 
	  <cybox:Association_Type xsi:type="maecVocabs:ActionObjectAssociationTypeVocab-1.0">output</cybox:Association_Type>
	</cybox:Associated_Object> 
  </cybox:Associated_Objects> 
</maecBundle:Action>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Raw Artifact Data</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> Artifact/Raw_Artifact
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/ArtifactObj/ArtifactObjectType/>CybOX::ArtifactObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture raw artifact data related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object/Related_Objects/Related_Object/</td>
	<td>Used to capture raw artifact data related to an Object that is associated with an Action (which is associated with a malware instance).</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Object id="maec-example-obj-1"> 
  <cybox:Properties xsi:type="ArtifactObj:ArtifactObjectType" type="Network Traffic"> 
    <ArtifactObj:Raw_Artifact>
	<![CDATA[11DF01000001000000000000057961686F6F03636F6D00000F00010011DF8180000100070007000E057961686F6F03636F6D00000F0001C00C000F000100001C20000E00010161026D78046D61696CC00CC00C000F000100001C20000600010162C02BC00C000F000100001C20000600010163C02BC00C000F000100001C20000600010164C02BC00C000F000100001C20000600010165C02BC00C000F000100001C20000600010166C02BC00C000F000100001C20000600010167C02BC00C0002000100016AB10006036E7336C00CC00C0002000100016AB10006036E7338C00CC00C0002000100016AB10006036E7331C00CC00C0002000100016AB10006036E7332C00CC00C0002000100016AB10006036E7333C00CC00C0002000100016AB10006036E7334C00CC00C0002000100016AB10006036E7335C00CC0290001000100000708000443C3A81FC0430001000100000708000442C461FAC05500010001000007080004D8273502C05500010001000007080004D8273503C0670001000100000708000442C45207C07900010001000007080004D8273501C08B00010001000007080004448ECAF7C08B00010001000007080004628936EDC09D00010001000007080004CEBE35BFC09D00010001000007080004D1BF7667C0D10001000100016312000444B48310C0E300010001000163120004448EFF10C0F50001000100016312000479659863C10700010001000163120004448EC43F]]> 
	</ArtifactObj:Raw_Artifact> 
  </cybox:Properties> 
</maecBundle:Object>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Registry Key Attributes</feature></th>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> WinRegistryKeyObj/Key
		<li> WinRegistryKeyObj/Hive
		<li> WinRegistryKeyObj/Values/Value/Name
		<li> WinRegistryKeyObj/Values/Value/Data
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/WinRegistryKeyObj/WindowsRegistryKeyObjectType/>CybOX::WinRegistryKeyObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture attributes of a single registry key related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture attributes of a single registry key related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture attributes of a single registry key related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture attributes of a single registry key related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<cybox:Associated_Object>
  <cybox:Properties xsi:type="WinRegistryKeyObj:WindowsRegistryKeyObjectType">
    <WinRegistryKeyObj:Key>Software\Microsoft\Windows\CurrentVersion\Run</WinRegistryKeyObj:Key>
	<WinRegistryKeyObj:Hive>HKEY_CURRENT_USER</WinRegistryKeyObj:Hive>
	<WinRegistryKeyObj:Values>
	  <WinRegistryKeyObj:Value>
	    <WinRegistryKeyObj:Name>Zcxaxz</WinRegistryKeyObj:Name>
		<WinRegistryKeyObj:Data>%AppData%\Zcxaxz.exe</WinRegistryKeyObj:Data>
	  </WinRegistryKeyObj:Value>
	</WinRegistryKeyObj:Values>
  </cybox:Properties>
</cybox:Associated_Object>
{% endhighlight %}
    </td>
  </tr>
</table>

<table class="table-features">
  <tr style="background-color:#0040FF">
    <th colspan="2"><feature>Universal Resource Indicator (URI)</feature></th>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>MAEC/CybOX Object Elements</th>
    <th>MAEC/CybOX Schemas</th>
  </tr>
  <tr>
    <td>
      <ul>
	    <li> URI/Value
	  </ul>
    </td>
    <td>
      <ul>
        <li> <a href=http://maecproject.github.io/data-model/4.1/URIObj/URIObjectType/>CybOX::URIObj</a>
	  </ul>
    </td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th>Typical MAEC Schema Locations</th>
	<th>Description</th>
  </tr>
  <tr>   
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes</td>
	<td>Used to capture a single URI associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes</td>
	 <td>Used to capture a single URI associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object</td>
	 <td>Used to capture a single URI related to an Action associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object</td>
	 <td>Used to capture a single URI related to an Object associated with a malware instance.</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object</td>
	<td>Used to capture a single URI related to an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object</td>
	<td>Used to capture a single URI related to an Object in an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml %}
<maecBundle:Malware_Instance_Object_Attributes>
  <cybox:Properties xsi:type="URIObj:URIObjectType"> 
    <URIObj:Value>http://samsonikonyou.ru:8080/navigator/jueoaritjuir.php</URIObj:Value> 
  </cybox:Properties> 
</maecBundle:Malware_Instance_Object_Attributes>
{% endhighlight %}
    </td>
  </tr>
</table>
		   






















