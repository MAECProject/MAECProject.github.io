---
layout: flat
title: Creating a MAEC Bundle
summary: Before looking at examples involving actual malware, we outline the general process of capturing basic malware analysis results in a MAEC Bundle.  It will often be the case that individual malware analysis tools automatically generate much of the content of a MAEC Bundle; however, as we will discuss, an analyst also typically plays a role in capturing results. 
---

Before looking at examples involving actual malware, we outline the general process of capturing basic malware analysis results in a MAEC Bundle.  It will often be the case that individual malware analysis tools automatically generate much of the content of a MAEC Bundle; however, as we will discuss, an analyst also typically plays a role in capturing results. 


## Data model

<img src="MAEC_Bundle.png" alt="Empty MAEC Bundle" class="aside-text"/>

To begin, a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) is created, as shown in the figure.  A MAEC Bundle requires just two attributes:

1.    Globally unique identifier. 
    The recommended form for MAEC identifier attributes is "maec-namespace-   entity_type-unique_identifier" where the namespace is optional and specified by the producer.  It is recommended that the namespace be meaningful and that the identifier be sequential.  For example, the identifier "maec-anubis_to_maec-act-1" uses the namespace "anubis_to_maec" to specify that the Anubis to MAEC translator tool  was used to create the MAEC output.  It is also recommended that the same namespace be used throughout a Bundle, although this is not required.

2.    MAEC schema version. 
    The MAEC schema version specifies the version used to create the Bundle.

As indicated by the placeholders in the figure, Objects, Actions, and Behaviors will be added as a result of analyses performed by tools and analysts.


## XML

{% highlight xml linenos %}
<stix:TTP xsi:type="ttp:TTPType" id="example:ttp-7d9fe1f7-429d-077e-db51-92c70b8da45a">
    <ttp:Title>Poison Ivy Variant v4392-acc</ttp:Title>
    <ttp:Behavior>
        <ttp:Malware>
            <ttp:Malware_Instance xsi:type="stix-maec:MAEC4.1InstanceType">
                <ttp:Type xsi:type="stixVocabs:MalwareTypeVocab-1.0">Remote Access Trojan</ttp:Type>
                <ttp:Name>Poison Ivy Variant v4392-acc</ttp:Name>
                <stix-maec:MAEC>
                    <!-- MAEC Content Here --> 
                </stix-maec:MAEC>                        
            </ttp:Malware_Instance>
        </ttp:Malware>
    </ttp:Behavior>
</stix:TTP>
{% endhighlight %}

[Full XML](malware-characterization-using-maec.xml)

## Python

{% highlight python linenos %}
from stix.ttp import TTP, Behavior
from stix.extensions.malware.maec_4_1_malware import MAECInstance

maec_malware_instance = MAECInstance()
maec_malware_instance.add_name("Poison Ivy Variant v4392-acc")
maec_malware_instance.add_type("Remote Access Trojan")
maec_malware_instance.maec = __INSERT_MAEC_ETREE_HERE__

ttp = TTP(title="Poison Ivy Variant v4392-acc")
ttp.behavior = Behavior()
ttp.behavior.add_malware_instance(maec_malware_instance)

print ttp.to_xml()
{% endhighlight %}

[Full Python](malware-characterization-using-maec.py)

## Further Reading

