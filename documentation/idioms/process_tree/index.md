---
layout: flat
title: Capturing Process Tree Information
summary: This Idiom describes the process of an observed process tree of execution for a malware instance, as reported through a dynamic analysis or similar tool.
---

This Idiom describes the process of capturing the process tree of execution that was observed and reported for a malware instance by a dynamic analysis or similar tool. As with all analysis-derived results, those that come from dynamic analysis can be captured through the use of a MAEC Bundle. However, results pertaining to the process tree of execution for a malware instance will be captured exclusively through the use of the [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) entity.

## Scenario

In this scenario, a malicious PE binary has been analyzed through the freely available Anubis sandbox service, which provides information about the low-level actions that the PE binary performs when executed and also the process tree of execution that was seen. Note that in this example, we'll be covering only the capture of the process tree - for information on the capture of API calls and actions, please see the [Capturing Dynamic Analysis Results ](../dynamic_analysis) Idiom. Also, for the sake of brevity, we will assume that the observed process tree involves only two different processes - the process first spawned when the malicious binary was executed ("first_process.exe"), and a child process spawned by this process ("malproc.exe"). Accordingly, let's assume that the first (root) process performs a single Action of creating a file.

## Data Model

The following are the important MAEC data model constructs used in this idiom:

* [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType): the Process Tree entity is used to characterize an observed process tree of execution for a malware instance, and is captured in a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType).

* [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType): the Process Tree Node is used to capture a single node in the [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType), or in other words the details around a single process.

Let's discuss the [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType) in more detail. Firstly, it's important to note that this entity derives from the [CybOX Process Object](/data-model/{{site.current_version}}/ProcessObj/ProcessObjectType), so that it encompasses all of the Process Object fields, including the following that are commonly utilized:

*	*PID*. The PID field specifies the Process ID, or PID, of the process.

*	*Name*. The Name field specifies the name of the process.

*	*Image_Info*. The Image_Info field specifies information about the image associated with the process, such as its file name and path.

Additionally, the following fields are extensions added in the [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType):

1.	*Initiated_Actions*. The Initiated_Actions field captures, via references, the actions (found inside the top-level Actions element, or an Action Collection inside the top-level Collections element) initiated by the Process.

2.	*Spawned_Process*. The Spawned_Process field captures a single child process spawned by this process.

3.	*Injected_Process*. The Injected_Process field captures a single process that was injected by this process.

## Process

As with many of the other Idioms, the first step is to create a [MAEC Package](/data-model/{{site.current_version}}/maecPackage/PackageType) with a [Malware Subject](/data-model/{{site.current_version}}/maecPackage/MalwareSubjectType) for capturing the information about the malware instance being analyzed. We should also add an [Analysis](/data-model/{{site.current_version}}/maecPackage/AnalysisType) entity to the Malware Subject to capture some details relating the particular analysis that we're performing. The information on this process is not covered in this idiom, but can be found in the corresponding [Creating a MAEC Package](../package_creation) and [Capturing Analysis Metadata](../analysis_metadata) idioms.

Next, a [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) is created. Once created, we must set the "content_type" attribute on the Bundle to define the type of content that it is characterizing.  In this case, since we're capturing output related to dynamic analysis, we should set it to a value of "dynamic analysis tool output". This is one of the values contained in the BundleContentTypeEnum enumeration used by this field. Finally, we should set the defined_subject attribute on the Bundle to a value of "false", since this Bundle will be contained in a Malware Subject, which has already defined the particular malware instance being characterized.

Now that we've set up the Bundle that will capture the process tree results, we can begin to populate it with these results. As mentioned in the introduction, we'll be using the [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) entity to capture the output of the observed process tree. Accordingly, since the [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) is intended to serve simply as the root of the process tree, we'll be using the [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType) entity to capture the information about the actual processes in the tree. 

Thus, the general process of building a [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) instance involves the following basic steps:

1.	Create the [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) instance by populating its corresponding "Process_Tree" field at the top-level of the Bundle that was previously created. 

2.	Set the root process in the "Root_Process" field of the process tree by using the [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType). 

3.	Set any defined properties on the root process, such as its process ID ("PID" field) or process name ("Name" field). For our example, we'll set the "Name" field to a value of "first_process.exe". 

4.	Define any processes that were spawned or injected by the root process using their respective "Spawned_Process" and "Injected_Process" fields and the [Process Tree Node](/data-model/{{site.current_version}}/maecBundle/ProcessTreeNodeType). For our example, we'll add a single "Spawned_Process" that corresponds to the one spawned by "first_process.exe". 

5.	Define any Actions that were initiated by the root process using the [Initated_Actions](/data-model/{{site.current_version}}/maecBundle/ActionReferenceListType) field and the corresponding [Action Reference](/data-model/{{site.current_version}}/cybox/ActionReferenceType) entity. The [Action Reference](/data-model/{{site.current_version}}/cybox/ActionReferenceType) is simply a reference, via its "action_id" field, to an Action that is defined elsewhere in the same [MAEC Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) that the [Process Tree](/data-model/{{site.current_version}}/maecBundle/ProcessTreeType) resides in. For our example, we'll add a single [Action Reference](/data-model/{{site.current_version}}/cybox/ActionReferenceType) instance to the [Initated_Actions](/data-model/{{site.current_version}}/maecBundle/ActionReferenceListType) field in order to refer to the "create file" Action that was initiated by the root process.

6.	Repeat steps 3-5 for any spawned or injected processes, as well as their children, defined in the respective "Spawned_Process" and "Injected_Process" fields of the root process.  For our example, we'll set the "Name" field of the spawned process that we added to a value of "malproc.exe", for representing the identity of the process spawned by "first_process.exe".

With the [Bundle](/data-model/{{site.current_version}}/maecBundle/BundleType) populated with the process tree information, the final step is to add it to the Malware Subject. To do, we'll use the [Findings_Bundles](/data-model/{{site.current_version}}/maecPackage/FindingsBundleListType) field, and specifically will populate its child "Bundle" field with the Bundle that we've constructed.

## XML

{% highlight xml linenos %}
<maecBundle:Process_Tree>
	<maecBundle:Root_Process id="example:process-b61b6bd3-3489-4db9-8558-a148526e96be">
		<ProcessObj:Name>first_process.exe</ProcessObj:Name>
		<maecBundle:Initiated_Actions>
			<maecBundle:Action_Reference action_id="example:action-68f87759-45f4-4e2e-b3a1-1edf15282db5"/>
		</maecBundle:Initiated_Actions>
		<maecBundle:Spawned_Process id="example:process-d3b74b23-01e4-408e-a29f-fdb45c40bed4">
			<ProcessObj:Name>malproc.exe</ProcessObj:Name>
		</maecBundle:Spawned_Process>
	</maecBundle:Root_Process>
</maecBundle:Process_Tree>
{% endhighlight %}

[Full XML](maec_process_tree.xml)
## Python

{% highlight python linenos %}
# Create the first, create file action
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
{% endhighlight %}

[Full Python](maec_process_tree.py)

## Further Reading
* [Creating a MAEC Bundle] (../bundle_creation)
* [Creating a MAEC Package] (../package_creation)
* [Capturing Dynamic Analysis Results] (../dynamic_analysis)