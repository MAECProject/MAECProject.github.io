---
layout: flat
title: Common Features
---

This page contains commonly characterized features - whether statically, dynamically, or manually identified in malware - along with their mappings to MAEC/CybOX object elements, the associated MAEC/CybOX schemas, the typical MAEC schema locations of the object elements (specified via a quasi-XPath like expression), and an explicit XML representation example. Note that all object elements are characterized through their Properties field, and that only the most commonly used object elements are listed for each feature (please refer to the applicable schemas for the complete lists).  

<br>

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
        <li> <a href=http://maecproject.github.io/data-model/4.1/FileObj/FileObjectType/>CybOX:FileObj</a>
   	    <li> <a href=http://maecproject.github.io/data-model/4.1/WinFileObj/WindowsFileObjectType/>CybOX:WinFileObj</a>
		<li> <a href=http://maecproject.github.io/data-model/4.1/WinExecutableFileObj/WindowsExecutableFileObjectType/>CybOX:WinExecFileObj</a>
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
        <li> <a href=http://maecproject.github.io/data-model/4.1/URIObj/URIObjectType/>CybOX:URIObj</a>
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
        <li> <a href=http://maecproject.github.io/data-model/4.1/CodeObj/CodeObjectType/>CybOX:CodeObj</a>
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