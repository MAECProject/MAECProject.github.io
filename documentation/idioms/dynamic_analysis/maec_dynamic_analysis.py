# Code for MAEC Static Analysis Idiom
from maec.package.package import Package
from maec.package.malware_subject import MalwareSubject
from maec.package.analysis import Analysis, Source
from maec.utils import IDGenerator, set_id_method
from cybox.core import Object
from cybox.objects.win_executable_file_object import WinExecutableFile, PEHeaders, PEOptionalHeader
from cybox.common import ToolInformation
from maec.bundle.bundle import Bundle

# Set up the necessary Package, Malware Subject, Analysis Bundle Instances
set_id_method(IDGenerator.METHOD_INT)
p = Package()
ms = MalwareSubject()
b = Bundle()
a = Analysis()

# Set the Malware_Instance_Object_Attributes on the Malware Subject
ms.malware_instance_object_attributes = Object()
ms.malware_instance_object_attributes.properties = WinExecutableFile()
ms.malware_instance_object_attributes.properties.file_name = "dg003_improve_8080_V132.exe"
ms.malware_instance_object_attributes.properties.size_in_bytes = "196608"
ms.malware_instance_object_attributes.properties.add_hash("4EC0027BEF4D7E1786A04D021FA8A67F")

# Populate the Analysis with the metadata relating to the Analysis that was performed
a.method = "static"
a.type_ = "triage"
a.summary = "A basic static triage of the subject binary using PEiD."
a.set_findings_bundle(b.id_)
a.source = Source()
a.source.name = "Frankie Li"
a.source.url = "http://www.sans.org/reading_room/whitepapers/malicious/detailed-analysis-advanced-persistent-threat-malware_33814"
t = ToolInformation()
t.name = "PEiD"
t.version = "0.94"
a.add_tool(t)

# Set the requisite attributes on the Bundle and populate it with the Static Analysis findings
b.defined_subject = False
b.content_type = "static analysis tool output"
o = Object()
o.properties = WinExecutableFile()
o.properties.headers = PEHeaders()
o.properties.headers.optional_header = PEOptionalHeader()
o.properties.headers.optional_header.major_linker_version = "06"
o.properties.headers.optional_header.minor_linker_version = "00"
o.properties.headers.optional_header.address_of_entry_point = "036418"
o.properties.headers.optional_header.subsystem = "Windows_GUI"

# Build up the full Package/Malware Subject/Analysis/Bundle hierarchy
p.add_malware_subject(ms)
b.add_object(o)
ms.add_analysis(a)
ms.add_findings_bundle(b)

# Output the built up Package to XML
print p.to_xml()

