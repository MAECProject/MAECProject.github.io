---
layout: flat
title: Capturing Higher-level Analysis Results
summary: This Idiom describes the process of capturing results of in-depth malware analysis, such as that which characterizes the capabilities or behaviors exhibited by the malware.
---

This Idiom describes the process of capturing results of in-depth malware analysis, such as that which characterizes the capabilities or behaviors exhibited by the malware. 

## Scenario

In this scenario, a malicious PE binary has been manually analyzed through the use of a disassembler tool. As part of this analysis, it has been discovered that the malware instance contains a keylogging capability, as well as a Windows-hook based behavior that functions as the implementation of this capability.

## Data model

The following are the important MAEC data model constructs used in this idiom:

* [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType): the capability entity is used to characterize the keylogging capability possessed by the malware instance. 
* [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType): the behavior entity is used to characterize the particular implementation of the keylogging capability possessed by the malware instance.

## Process

As with many of the other Idioms, the first step is to create a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) with a [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) for capturing the information about the malware instance being analyzed. We should also add an [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity to the Malware Subject to capture some details relating the particular analysis that we're performing. The information on this process is not covered in this idiom, but can be found in the corresponding [Creating a MAEC Package](../package_creation) and [Capturing Analysis Metadata](../analysis_metadata) idioms.

Next, a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) is created. Once created, we must set the *content_type* attribute on the Bundle to define the type of content that it is characterizing.  In this case, since we're capturing the output of manual analysis that was performed on the binary, we should set it to a value of `manual analysis output`. This is one of the values contained in the BundleContentTypeEnum enumeration used by this field. Finally, we should set the defined_subject attribute on the Bundle to a value of `false`, since this Bundle will be contained in a Malware Subject, which has already defined the particular malware instance being characterized.

### Capturing Behaviors

Now that we've set up the Bundle that will capture the higher-level analysis results, we can begin to populate it with these results. Since we're capturing a malware capability and behavior in our example scenario, we'll use the corresponding MAEC [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType) and [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType) entities. First, let's discuss the steps involved in capturing the Windows-hook based behavior that serves as the implementation of the keylogging capability:

1.	We'll need to add an instance of a [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType) to the top-level [Behaviors](/data-model/{{site.current_version}}/maecBundle/BehaviorListType) list-type field found in the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that we've previously defined.
2.	Next, we'll need to capture the details of this [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType). In the case of this example scenario, we know that the malware instance adds a Windows-hook, the act of which can be represented with a [Malware Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType). The process of adding Actions is not captured in detail here as it is documented in the [Capturing Dynamic Analysis Results] (../dynamic_analysis) idiom. However, let's assume that we've added an "add windows hook" [Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType) to the top-level [Actions](/data-model/{{site.current_version}}/maecBundle/ActionListType) list-type entity found at the root level of the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that we've previously defined. 
3.	We now need to link this [Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType) to the [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType) in order to specify the context of how it is implemented. This is achieved by populating the [Action_Composition](/data-model/{{site.current_version}}/maecBundle/BehavioralActionsType) field in the [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType), which is used to express the [Actions](/data-model/{{site.current_version}}/maecBundle/MalwareActionType) that compose the [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType). In this case, we'll need to reference the "add windows hook" [Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType) since it is defined at the top-level of the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType). To do so, we'll make use of a single instance of the  [Action_Reference](/data-model/{{site.current_version}}/maecBundle/BehavioralActionReferenceType) field for this purpose; here, we will populate the *action_id* field with the ID of the [Action](/data-model/{{site.current_version}}/maecBundle/MalwareActionType) that we are referencing.

### Capturing Capabilities

Next, let's explore the steps involved in capturing the keylogging capability; as seen below, this is quite similar to the steps for capturing the details of the behavior:

1.	We'll need to add an instance of a [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType) to the top-level [Capabilities](/data-model/{{site.current_version}}/maecBundle/CapabilityListType) list-type field found in the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that we've previously defined. 
2.	Next, with the [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType) instantiated, we'll need to define the broad type of malware capability that it refers to. This is accomplished through the use of the *name* attribute, which makes use of the `MalwareCapabilityEnum-1.0` enumeration that captures a set of high-level malware capabilities such as persistence, command and control, etc. As of MAEC v4.1, we've defined an initial set of these capabilities, along with their children that we refer to as "objectives" (see the full hierarchy [here](https://github.com/MAECProject/schemas/wiki/Malware-Capabilities)). In this case, keylogging refers to an objective that falls under the spying capability, so we would set the *name* attribute to a value of `spying`.
3.	With the information on the top-level (i.e., spying) capability captured, the next step is to capture the fact that we're referring to keylogging. As such, we need to go through the child objectives of the spying capability (full hierarchy [here](https://github.com/MAECProject/schemas/wiki/Malware-Capabilities)) and see if there is one that matches the concept of keylogging. Going through this list, we see that we have a "Capture Keyboard Input" tactical objective, which aligns perfectly with keylogging.  
4.	Having found a corresponding objective in MAEC's hierarchy, we'll need to add this objective to the [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType) that we've already defined. To do so, we'll add an instance of a [Tactical_Objective](/data-model/{{site.current_version}}/maecBundle/CapabilityObjectiveType) to the [Capability](/data-model/{{site.current_version}}/maecBundle/CapabilityType). Inside of this [Tactical_Objective](/data-model/{{site.current_version}}/maecBundle/CapabilityObjectiveType), we'll need to populate the *Name* field to capture the name of the objective that we're capturing. In the case of this example scenario, we'll use a value of `capture keyboard input`, and accordingly we'll need to set the *xsi:type* attribute on this field to a value of `SpyingTacticalObjectivesVocab-1.0`, since it is found in the [Spying Tactical Objectives Vocabulary](/data-model/{{site.current_version}}/maecVocabs/SpyingTacticalObjectivesVocab-1.0/).
5.	Finally, we need to link the [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType) that we previously created to the  [Tactical Objective](/data-model/{{site.current_version}}/maecBundle/CapabilityObjectiveType) defined in the previous step, in order to define how it was implemented in the malware instance. To do so, we'll make use of a single instance of the  [Behavior_Reference](/data-model/{{site.current_version}}/maecBundle/BehaviorReferenceType) field for this purpose; here, we will populate the *behavior_idref* attribute with the ID of the [Behavior](/data-model/{{site.current_version}}/maecBundle/BehaviorType) that we are referencing.


## XML

{% highlight xml linenos %}
<maecBundle:Capabilities>
  <maecBundle:Capability id="example:capability-dc4a7c3a-4c54-45f5-8110-7e4fcee3b462" name="spying">
    <maecBundle:Tactical_Objective id="example:tactical_objective-065bee75-5e43-4c66-918a-57eba1dab08c">
      <maecBundle:Name xsi:type="maecVocabs:SpyingTacticalObjectivesVocab-1.0">capture keyboard input</maecBundle:Name>
      <maecBundle:Behavior_Reference behavior_idref="example:behavior-cfb4d731-c6e2-4c8e-808d-111e1ba66962"/>
    </maecBundle:Tactical_Objective>
  </maecBundle:Capability>
</maecBundle:Capabilities>
<maecBundle:Behaviors>
  <maecBundle:Behavior id="example:behavior-cfb4d731-c6e2-4c8e-808d-111e1ba66962">
    <maecBundle:Action_Composition>
	  <maecBundle:Action_Reference action_id="example:action-a48e58bb-f35d-4bf6-bb16-0e74061ac47e"/>
	</maecBundle:Action_Composition>
  </maecBundle:Behavior>
</maecBundle:Behaviors>
{% endhighlight %}

[Full XML](maec_in_depth_analysis.xml)
## Python

{% highlight python linenos %}

{% endhighlight %}

[Full Python](maec_in_depth_analysis.py)

## Further Reading
* [Creating a MAEC Bundle] (../bundle_creation)
* [Creating a MAEC Package] (../package_creation)
* [Capturing Dynamic Analysis Results] (../dynamic_analysis)