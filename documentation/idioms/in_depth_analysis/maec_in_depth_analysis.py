# Code for MAEC In-depth Analysis Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from maec.package.analysis import Analysis
from maec.bundle.bundle import Bundle, BehaviorReference
from maec.bundle.malware_action import MalwareAction
from maec.bundle.capability import Capability, CapabilityObjective, CapabilityList
from maec.bundle.behavior import Behavior, BehavioralActions, BehavioralActionReference
from cybox.core import Object, AssociatedObject, AssociatedObjects
from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.objects.win_hook_object import WinHook
from cybox.common import VocabString

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

# Populate the Analysis with the metadata relating to the Analysis that was performed
a.method = "static"
a.type_ = "in-depth"
a.set_findings_bundle(b.id_)

# Set the requisite attributes on the Bundle and populate it with the In-depth Analysis findings
b.defined_subject = False
b.content_type = "manual analysis output"

# Create the add windows hook action
act = MalwareAction()
act.name = "add windows hook"
act.name.xsi_type = "maecVocabs:HookingActionNameVocab-1.0"
act.associated_objects = AssociatedObjects()
o1 = AssociatedObject()
o1.properties = WinHook()
o1.properties.type_ = "WH_KEYBOARD_LL"
o1.association_type = VocabString()
o1.association_type.value = "output"
o1.association_type.xsi_type = "maecVocabs:ActionObjectAssociationTypeVocab-1.0"
act.associated_objects.append(o1)

# Create the behavior
bhv = Behavior()
bhv.action_composition = BehavioralActions()
bhv.action_composition.action_reference = [BehavioralActionReference()]
bhv.action_composition.action_reference[0].action_id = act.id_

# Create the capability
cap = Capability()
cap.name = "spying"
obj = CapabilityObjective()
obj.name = VocabString()
obj.name.value = "capture keyboard input"
obj.name.xsi_type = "maecVocabs:SpyingTacticalObjectivesVocab-1.0"
obj.behavior_reference = [BehaviorReference()]
obj.behavior_reference[0].behavior_idref = bhv.id_
cap.add_tactical_objective(obj)

# Build up the full Package/Malware Subject/Analysis/Bundle hierarchy
p.add_malware_subject(ms)
b.add_action(act)
b.add_behavior(bhv)
b.add_capability(cap)
ms.add_analysis(a)
ms.add_findings_bundle(b)

# Output the built up Package to XML
print p.to_xml(namespace_dict={"example.com" : "example"})

