---
layout: flat
title: Creating a MAEC Bundle
summary: Before looking at examples involving actual malware, we outline the general process of capturing basic malware analysis results in a MAEC Bundle.  It will often be the case that individual malware analysis tools automatically generate much of the content of a MAEC Bundle; however, as we will discuss, an analyst also typically plays a role in capturing results. 
---

Before looking at examples involving actual malware, we outline the general process of capturing basic malware analysis results in a MAEC Bundle.  It will often be the case that individual malware analysis tools automatically generate much of the content of a MAEC Bundle; however, as we will discuss, an analyst also typically plays a role in capturing results. 


## Data model

<img src="maec_bundle.png" alt="Empty MAEC Bundle" class="aside-text"/>

To begin, a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) is created, as shown in the figure.  A MAEC Bundle requires just two attributes:

1.    Globally unique identifier. 
    The recommended form for MAEC identifier attributes is "maec-namespace-   entity_type-unique_identifier" where the namespace is optional and specified by the producer.  It is recommended that the namespace be meaningful and that the identifier be sequential.  For example, the identifier "maec-anubis_to_maec-act-1" uses the namespace "anubis_to_maec" to specify that the Anubis to MAEC translator tool  was used to create the MAEC output.  It is also recommended that the same namespace be used throughout a Bundle, although this is not required.

2.    MAEC schema version. 
    The MAEC schema version specifies the version used to create the Bundle.

As indicated by the placeholders in the figure, Objects, Actions, and Behaviors will be added as a result of analyses performed by tools and analysts.


## XML

{% highlight xml linenos %}
<maecBundle:MAEC_Bundle
 id="maec-example-bnd-1" schema_version="4.1">
 </maecBundle:MAEC_Bundle>
{% endhighlight %}

## Python

{% highlight python linenos %}
from maec.bundle.bundle import Bundle

b = Bundle()
{% endhighlight %}

## Further Reading

