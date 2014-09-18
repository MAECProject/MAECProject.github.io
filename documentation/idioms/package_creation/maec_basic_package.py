# Code for MAEC Basic Package Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from cybox.core import Object
from cybox.objects.file_object import File

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

# Output the built up Package to XML
print p.to_xml()

