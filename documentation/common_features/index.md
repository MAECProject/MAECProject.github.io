---
layout: flat
title: Common Features
---

This page contains commonly characterized features - whether statically, dynamically, or manually identified in malware - along with their mappings to MAEC/CybOX object elements, the associated MAEC/CybOX schemas, the typical MAEC schema locations of the object elements (specified via a quasi-XPath like expression) and associated attributes (captured in [square brackets]), and an explicit XML representation example. Only the most commonly used object elements are listed for each feature; please refer to the applicable schemas for the complete lists.  

### File Attributes

<table class="table-features">
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
    <td>MAEC_Package/Malware_Subjects/Malware_Subject/Malware_Subject/Malware_Instance_Object_Attributes/Properties[xsi:type=”{ObjectType}”]</td>
	<td>Used to capture a single file associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Malware_Instance_Object_Attributes/Properties[xsi:type=”{ObjectType}”]</td>
	 <td>Used to capture a single file associated with a malware instance.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Actions/Action/Associated_Objects/Associated_Object/Properties[xsi:type=”{ObjectType}”]</td>
	 <td>Used to capture a single file associated with an Action.</td>
  </tr>
  <tr>
	 <td>MAEC_Bundle/Objects/Object/Properties[xsi:type=”{ObjectType}”]</td>
	 <td>Used to capture a single file associated with a malware instance, including those that represent some extracted feature (e.g., strings).</td>
  </tr>
  <tr>   <td>MAEC_Bundle/Collections/Action_Collections/Action_Collection/Action_List/Action/Associated_Objects/Associated_Object/Properties[xsi:type=”{ObjectType}”]</td>
	<td>Used to capture a single file associated with an Action in an Action Collection.</td>
  </tr>
  <tr>
    <td>MAEC_Bundle/Collections/Object_Collections/Object_Collection/Object_List/Object/Properties[xsi:type=”{ObjectType}”]</td>
	<td>Used to capture a single file as part of an Object Collection.</td>
  </tr>
  <tr style="background-color:#A9D0F5">
    <th colspan="2">MAEC/CybOX XML Representation Example</th>
  </tr>
  <tr>
    <td colspan="2">
{% highlight xml linenos %}
<cybox: Associated_Object id="maec-example-obj-2"> 
<cybox:Properties xsi:type="WinExecFileObj:WindowsExecutableFileObjectType"> 
<FileObj:File_Name>ws2help.PNF</FileObj:File_Name> 
<FileObj:File_Path condition="FitsPattern" pattern_type="Regex">^C:\Documents and Settings\\s+user\s+\Local Settings\Application\Data</FileObj:Full_Path>
<FileObj:Size_In_Bytes>196608</FileObj:Size_In_Bytes> </cybox:Properties>
</cybox: Associated_Object>
{% endhighlight %}
    </td>
  </tr>
</table>
    	
		   
