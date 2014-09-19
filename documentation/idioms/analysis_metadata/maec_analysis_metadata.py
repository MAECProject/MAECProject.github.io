# Code for MAEC Analysis Metadata Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from maec.package.analysis import Analysis
from cybox.core import Object
from cybox.common import ToolInformation, VocabString
from cybox.objects.win_executable_file_object import WinExecutableFile

# Set up the necessary Package, Malware Subject, Analysis instances
p = Package()
ms = MalwareSubject()
a1 = Analysis()
a2 = Analysis()

# Set the Malware_Instance_Object_Attributes on the Malware Subject
ms.malware_instance_object_attributes = Object()
ms.malware_instance_object_attributes.properties = WinExecutableFile()
ms.malware_instance_object_attributes.properties.size_in_bytes = "210564"
ms.malware_instance_object_attributes.properties.add_hash("B6C39FF68346DCC8B67AA060DEFE40C2")

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

# Build up the full Package/Malware Subject/Analysis hierarchy
p.add_malware_subject(ms)
ms.add_analysis(a1)
ms.add_analysis(a2)

# Output the built up Package to XML
print p.to_xml()

