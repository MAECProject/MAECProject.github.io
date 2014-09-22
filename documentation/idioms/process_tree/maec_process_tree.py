# Code for MAEC Process Tree Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from maec.package.analysis import Analysis
from maec.bundle.bundle import Bundle
from maec.bundle.malware_action import MalwareAction
from maec.bundle.process_tree import ProcessTree, ProcessTreeNode
from cybox.core import Object, AssociatedObject, AssociatedObjects
from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.common import ToolInformation, VocabString

# Set up the necessary Package, Malware Subject, Analysis Bundle Instances
p = Package()
ms = MalwareSubject()
b = Bundle()
a = Analysis()

# Set the Malware_Instance_Object_Attributes on the Malware Subject
ms.malware_instance_object_attributes = Object()
ms.malware_instance_object_attributes.properties = WinExecutableFile()
ms.malware_instance_object_attributes.properties.size_in_bytes = "251904"
ms.malware_instance_object_attributes.properties.add_hash("5247001dafe411802b1a40e763d9a221")
ms.malware_instance_object_attributes.properties.add_hash("7ff89166e226845e9fc52cb711eb5b37d004a0e5")

# Populate the Analysis with the metadata relating to the Analysis that was performed
a.method = "dynamic"
a.type_ = "triage"
a.set_findings_bundle(b.id_)
t = ToolInformation()
t.name = "Anubis"
t.vendor = "ISECLab"
a.add_tool(t)

# Set the requisite attributes on the Bundle and populate it with the Dynamic Analysis findings
b.defined_subject = False
b.content_type = "dynamic analysis tool output"

# Create the create file action initiated by the root process
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

# Create the Process Tree
p_tree = ProcessTree()

# Create the root process
root_p = ProcessTreeNode()
root_p.name = "first_process.exe"
root_p.add_initiated_action(act1.id_)

# Create the spawned process
spawned_p = ProcessTreeNode()
spawned_p.name = "malproc.exe"

# Add the spawned process to the root process
root_p.add_spawned_process(spawned_p)

# Set the root process in the process_tree
p_tree.set_root_process(root_p)

# Build up the full Package/Malware Subject/Analysis/Bundle hierarchy
p.add_malware_subject(ms)
b.add_action(act1)
b.set_process_tree(p_tree)
ms.add_analysis(a)
ms.add_findings_bundle(b)

# Output the built up Package to XML
print p.to_xml()

