# Code for MAEC AV Classification Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from maec.package.analysis import Analysis
from maec.bundle.bundle import Bundle
from maec.bundle.av_classification import AVClassification
from cybox.core import Object
from cybox.objects.win_executable_file_object import WinExecutableFile

# Set up the necessary Package, Malware Subject, Analysis Bundle Instances
p = Package()
ms = MalwareSubject()
b = Bundle()
a = Analysis()

# Set the Malware_Instance_Object_Attributes on the Malware Subject
ms.malware_instance_object_attributes = Object()
ms.malware_instance_object_attributes.properties = WinExecutableFile()
ms.malware_instance_object_attributes.properties.add_hash("076e5b2bae0b4b3a3d81c85610b95cd4")
ms.malware_instance_object_attributes.properties.add_hash("4484e08903744ceeaedd8f5e1bfc06b2c4688e76")

# Populate the Analysis with the metadata relating to the Analysis that was performed
a.method = "static"
a.type_ = "triage"
a.set_findings_bundle(b.id_)

# Set the requisite attributes on the Bundle
b.defined_subject = False
b.content_type = "static analysis tool output"

# Create the AV Classifications
av1 = AVClassification()
av1.name = "Microsoft"
av1.classification_name = "PWS:Win32/Zbot.gen!B"
av2 = AVClassification()
av2.name = "Symantec"
av2.classification_name = "Backdoor.Paproxy"
av3 = AVClassification()
av3.name = "TrendMicro"
av3.classification_name = "TSPY_ZBOT.TD"

# Add the AV classifications to the Bundle
b.add_av_classification(av1)
b.add_av_classification(av2)
b.add_av_classification(av3)

# Build up the full Package/Malware Subject/Analysis/Bundle hierarchy
p.add_malware_subject(ms)
ms.add_analysis(a)
ms.add_findings_bundle(b)

# Output the built up Package to XML
print p.to_xml()

