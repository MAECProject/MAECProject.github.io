# Code for MAEC Basic Bundle Idiom
from maec.bundle.bundle import Bundle
from cybox.core import Object
from cybox.objects.pdf_file_object import PDFFile

# Instantiate the Bundle and populate its required attributes
# The ID generation is handled automatically by python-maec
b = Bundle()
b.defined_subject = "True"

# Populate the Malware_Instance_Object_Attributes of the Bundle with the properties of the PDF file
b.malware_instance_object_attributes = Object()
b.malware_instance_object_attributes.properties = PDFFile()
b.malware_instance_object_attributes.properties.file_name = "User_Manual.pdf"
b.malware_instance_object_attributes.properties.size_in_bytes = "509328"
b.malware_instance_object_attributes.properties.version = "1.6"

print b.to_xml()