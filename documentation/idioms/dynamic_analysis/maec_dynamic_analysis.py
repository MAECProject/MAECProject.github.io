# Code for MAEC Dynamic Analysis Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from maec.package.analysis import Analysis
from maec.bundle.bundle import Bundle
from maec.bundle.malware_action import MalwareAction
from cybox.core import Object, AssociatedObject, AssociatedObjects
from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.objects.win_mutex_object import WinMutex
from cybox.common import ToolInformation, VocabString

# Set up the necessary Package, Malware Subject, Analysis Bundle Instances
p = Package()
ms = MalwareSubject()
b = Bundle()
a = Analysis()

# Set the Malware_Instance_Object_Attributes on the Malware Subject
ms.malware_instance_object_attributes = Object()
ms.malware_instance_object_attributes.properties = WinExecutableFile()
ms.malware_instance_object_attributes.properties.size_in_bytes = "210564"
ms.malware_instance_object_attributes.properties.add_hash("B6C39FF68346DCC8B67AA060DEFE40C2")
ms.malware_instance_object_attributes.properties.add_hash("D55B0FB96FAD96D203D10850469489FC03E6F2F7")

# Populate the Analysis with the metadata relating to the Analysis that was performed
a.method = "dynamic"
a.type_ = "triage"
a.set_findings_bundle(b.id_)
t = ToolInformation()
t.name = "ThreatExpert"
t.vendor = "ThreatExpert"
a.add_tool(t)

# Set the requisite attributes on the Bundle and populate it with the Dynamic Analysis findings
b.defined_subject = False
b.content_type = "dynamic analysis tool output"

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

# Build up the full Package/Malware Subject/Analysis/Bundle hierarchy
p.add_malware_subject(ms)
b.add_action(act1)
b.add_action(act2)
ms.add_analysis(a)
ms.add_findings_bundle(b)

# Output the built up Package to XML
print p.to_xml()

