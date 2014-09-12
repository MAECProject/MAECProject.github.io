require 'bundler'
require 'fileutils'
require 'liquid'
require 'maec_schema_spy'

$destination = "data-model"

$maec_prefixes = ['maecBundle', 'maecPackage',
                  'maecVocabs', 'maecContainer']

$maec_uri = "http://maec.readthedocs.org/en/latest/api/"
$cybox_uri = "http://cybox.readthedocs.org/en/latest/"

$maec_links = {
    "maecBundle:APICallType" => "bundle/malware_action.html#maec.bundle.malware_action.APICall",
    "maecBundle:AVClassificationType" => "bundle/av_classification.html#maec.bundle.av_classification.AVClassification",
    "maecBundle:AVClassificationsType" => "bundle/av_classification.html#maec.bundle.av_classification.AVClassifications",
    "maecBundle:ActionCollectionListType" => "bundle/bundle.html#maec.bundle.bundle.ActionCollectionList",
    "maecBundle:ActionCollectionType" => "bundle/bundle.html#maec.bundle.bundle.ActionCollection",
    "maecBundle:ActionImplementationType" => "bundle/malware_action.html#maec.bundle.malware_action.ActionImplementation",
    "maecBundle:ActionListType" => "bundle/bundle.html#maec.bundle.bundle.ActionList",
    "maecBundle:ActionReferenceListType" => "bundle/action_reference_list.html#maec.bundle.action_reference_list.ActionReferenceList",
    "maecBundle:AssociatedCodeType" => "bundle/behavior.html#maec.bundle.behavior.AssociatedCode",
    "maecBundle:BaseCollectionType" => "bundle/bundle.html#maec.bundle.bundle.BaseCollection",
    "maecBundle:BehaviorCollectionListType" => "bundle/bundle.html#maec.bundle.bundle.BehaviorCollectionList",
    "maecBundle:BehaviorCollectionType" => "bundle/bundle.html#maec.bundle.bundle.BehaviorCollection",
    "maecBundle:BehaviorListType" => "bundle/bundle.html#maec.bundle.bundle.BehaviorList",
    "maecBundle:BehaviorPurposeType" => "bundle/behavior.html#maec.bundle.behavior.BehaviorPurpose",
    "maecBundle:BehaviorReferenceListType" => nil,
    "maecBundle:BehaviorReferenceType" => "bundle/behavior_reference.html#maec.bundle.behavior_reference.BehaviorReference",
    "maecBundle:BehaviorRelationshipListType" => nil,
    "maecBundle:BehaviorRelationshipType" => nil,
    "maecBundle:BehaviorType" => "bundle/behavior.html#maec.bundle.behavior.Behavior",
    "maecBundle:BehavioralActionEquivalenceReferenceType" => "bundle/behavior.html#maec.bundle.behavior.BehavioralActionEquivalenceReference",
    "maecBundle:BehavioralActionReferenceType" => "bundle/behavior.html#maec.bundle.behavior.BehavioralActionReference",
    "maecBundle:BehavioralActionType" => "bundle/behavior.html#maec.bundle.behavior.BehavioralAction",
    "maecBundle:BehavioralActionsType" => "bundle/behavior.html#maec.bundle.behavior.BehavioralActions",
    "maecBundle:BundleReferenceType" => "bundle/bundle_reference.html#maec.bundle.bundle_reference.BundleReference",
    "maecBundle:BundleType" => "bundle/bundle.html#maec.bundle.bundle.Bundle",
    "maecBundle:CVEVulnerabilityType" => "bundle/behavior.html#maec.bundle.behavior.CVEVulnerability",
    "maecBundle:CandidateIndicatorCollectionListType" => "bundle/bundle.html#maec.bundle.bundle.CandidateIndicatorCollectionList",
    "maecBundle:CandidateIndicatorCollectionType" => "bundle/bundle.html#maec.bundle.bundle.CandidateIndicatorCollection",
    "maecBundle:CandidateIndicatorCompositionType" => "bundle/candidate_indicator.html#maec.bundle.candidate_indicator.CandidateIndicatorComposition",
    "maecBundle:CandidateIndicatorListType" => "bundle/candidate_indicator.html#maec.bundle.candidate_indicator.CandidateIndicatorList",
    "maecBundle:CandidateIndicatorType" => "bundle/candidate_indicator.html#maec.bundle.candidate_indicator.CandidateIndicator",
    "maecBundle:CapabilityListType" => "bundle/capability.html#maec.bundle.capability.CapabilityList",
    "maecBundle:CapabilityObjectiveReferenceType" => "bundle/capability.html#maec.bundle.capability.CapabilityObjectiveReference",
    "maecBundle:CapabilityObjectiveRelationshipType" => "bundle/capability.html#maec.bundle.capability.CapabilityObjectiveRelationship",
    "maecBundle:CapabilityObjectiveType" => "bundle/capability.html#maec.bundle.capability.CapabilityObjective",
    "maecBundle:CapabilityPropertyType" => "bundle/capability.html#maec.bundle.capability.CapabilityProperty",
    "maecBundle:CapabilityReferenceType" => "bundle/capability.html#maec.bundle.capability.CapabilityReference",
    "maecBundle:CapabilityRelationshipType" => "bundle/capability.html#maec.bundle.capability.CapabilityRelationship",
    "maecBundle:CapabilityType" => "bundle/capability.html#maec.bundle.capability.Capability",
    "maecBundle:CollectionsType" => "bundle/bundle.html#maec.bundle.bundle.Collections",
    "maecBundle:ExploitType" => "bundle/behavior.html#maec.bundle.behavior.Exploit",
    "maecBundle:MalwareActionType" => "bundle/malware_action.html#maec.bundle.malware_action.MalwareAction",
    "maecBundle:MalwareEntityType" => "bundle/candidate_indicator.html#maec.bundle.candidate_indicator.MalwareEntity",
    "maecBundle:ObjectCollectionListType" => "bundle/bundle.html#maec.bundle.bundle.ObjectCollectionList",
    "maecBundle:ObjectCollectionType" => "bundle/bundle.html#maec.bundle.bundle.ObjectCollection",
    "maecBundle:ObjectListType" => "bundle/bundle.html#maec.bundle.bundle.ObjectList",
    "maecBundle:ObjectReferenceListType" => "bundle/object_reference.html#maec.bundle.object_reference.ObjectReferenceList",
    "maecBundle:ObjectReferenceType" => "bundle/object_reference.html#maec.bundle.object_reference.ObjectReference",
    "maecBundle:ParameterListType" => "bundle/malware_action.html#maec.bundle.malware_action.ParameterList",
    "maecBundle:ParameterType" => "bundle/malware_action.html#maec.bundle.malware_action.Parameter",
    "maecBundle:PlatformListType" => "bundle/behavior.html#maec.bundle.behavior.PlatformList",
    "maecBundle:ProcessTreeNodeType" => "bundle/process_tree.html#maec.bundle.process_tree.ProcessTreeNode",
    "maecBundle:ProcessTreeType" => "bundle/process_tree.html#maec.bundle.process_tree.ProcessTree",
    "maecPackage:ActionEquivalenceType" => "package/action_equivalence.html#maec.package.action_equivalence#ActionEquivalence",
    "maecPackage:AnalysisEnvironmentType" => "package/analysis.html#maec.package.analysis#AnalysisEnvironment",
    "maecPackage:AnalysisListType" => "package/malware_subject.html#maec.package.malware_subject#Analyses",
    "maecPackage:AnalysisSystemListType" => "package/analysis.html#maec.package.analysis#AnalysisSystemList",
    "maecPackage:AnalysisSystemType" => "package/analysis.html#maec.package.analysis#AnalysisSystem",
    "maecPackage:AnalysisType" => "package/analysis.html#maec.package.analysis#Analysis",
    "maecPackage:CapturedProtocolListType" => "package/analysis.html#maec.package.analysis#CapturedProtocolList",
    "maecPackage:CapturedProtocolType" => "package/analysis.html#maec.package.analysis#CapturedProtocol",
    "maecPackage:ClusterCompositionType" => "package/grouping_relationship.html#maec.package.grouping_relationship#ClusterComposition",
    "maecPackage:ClusterEdgeNodePairType" => "package/grouping_relationship.html#maec.package.grouping_relationship#ClusterEdgeNodePair",
    "maecPackage:ClusteringAlgorithmParametersType" => "package/grouping_relationship.html#maec.package.grouping_relationship#ClusteringAlgorithmParameters",
    "maecPackage:ClusteringMetadataType" => "package/grouping_relationship.html#maec.package.grouping_relationship#ClusteringMetadata",
    "maecPackage:CommentListType" => "package/analysis.html#maec.package.analysis#CommentList",
    "maecPackage:CommentType" => "package/analysis.html#maec.package.analysis#Comment",
    "maecPackage:DynamicAnalysisMetadataType" => "package/analysis.html#maec.package.analysis#DynamicAnalysisMetadata",
    "maecPackage:FindingsBundleListType" => "package/malware_subject.html#maec.package.malware_subject#FindingsBundleList",
    "maecPackage:GroupingRelationshipListType" => "package/grouping_relationship.html#maec.package.grouping_relationship#GroupingRelationshipList",
    "maecPackage:GroupingRelationshipType" => "package/grouping_relationship.html#maec.package.grouping_relationship#GroupingRelationship",
    "maecPackage:HypervisorHostSystemType" => "package/analysis.html#maec.package.analysis#HypervisorHostSystem",
    "maecPackage:InstalledProgramsType" => "package/analysis.html#maec.package.analysis#InstalledPrograms",
    "maecPackage:MalwareBinaryConfigurationStorageDetailsType" => "package/malware_subject.html#maec.package.malware_subject#MalwareBinaryConfigurationStorageDetails",
    "maecPackage:MalwareConfigurationDetailsType" => "package/malware_subject.html#maec.package.malware_subject#MalwareConfigurationDetails",
    "maecPackage:MalwareConfigurationObfuscationAlgorithmType" => "package/malware_subject.html#maec.package.malware_subject#MalwareConfigurationObfuscationAlgorithm",
    "maecPackage:MalwareConfigurationObfuscationDetailsType" => "package/malware_subject.html#maec.package.malware_subject#MalwareConfigurationObfuscationDetails",
    "maecPackage:MalwareConfigurationParameterType" => "package/malware_subject.html#maec.package.malware_subject#MalwareConfigurationParameter",
    "maecPackage:MalwareConfigurationStorageDetailsType" => "package/malware_subject.html#maec.package.malware_subject#MalwareConfigurationStorageDetails",
    "maecPackage:MalwareDevelopmentEnvironmentType" => "package/malware_subject.html#maec.package.malware_subject#MalwareDevelopmentEnvironment",
    "maecPackage:MalwareExceptionType" => nil,
    "maecPackage:MalwareSubjectListType" => "package/malware_subject.html#maec.package.malware_subject#MalwareSubjectList",
    "maecPackage:MalwareSubjectReferenceType" => "package/malware_subject_reference.html#maec.package.malware_subject_reference#MalwareSubjectReference",
    "maecPackage:MalwareSubjectRelationshipListType" => "package/malware_subject.html#maec.package.malware_subject#MalwareSubjectRelationshipList",
    "maecPackage:MalwareSubjectRelationshipType" => "package/malware_subject.html#maec.package.malware_subject#MalwareSubjectRelationship",
    "maecPackage:MalwareSubjectType" => "package/malware_subject.html#maec.package.malware_subject#MalwareSubject",
    "maecPackage:MetaAnalysisType" => "package/malware_subject.html#maec.package.malware_subject#MetaAnalysis",
    "maecPackage:MinorVariantListType" => "package/malware_subject.html#maec.package.malware_subject#MinorVariants",
    "maecPackage:NetworkInfrastructureType" => "package/analysis.html#maec.package.analysis#NetworkInfrastructure",
    "maecPackage:ObjectEquivalenceListType" => "package/object_equivalence.html#maec.package.analysis#ObjectEquivalenceList",
    "maecPackage:ObjectEquivalenceType" => "package/analysis.html#maec.package.analysis#ObjectEquivalence",
    "maecPackage:PackageType" => "package/package.html#maec.package.analysis#Package",
    "maecPackage:SourceType" => "package/analysis.html#maec.package.analysis#Source",
    "maecPackage:ToolListType" => "package/analysis.html#maec.package.analysis#ToolList",
    "maecContainer:ContainerType" => nil,
    "maecContainer:PackageListType" => nil,
    "maecVocabs:ActionObjectAssociationTypeVocab-1.0" => "nil",
    "maecVocabs:AntiBehavioralAnalysisPropertiesVocab-1.0" => "nil",
    "maecVocabs:AntiBehavioralAnalysisStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiBehavioralAnalysisTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiCodeAnalysisStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiCodeAnalysisTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiDetectionStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiDetectionTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiRemovalStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:AntiRemovalTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:AvailabilityViolationPropertiesVocab-1.0" => "nil",
    "maecVocabs:AvailabilityViolationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:AvailabilityViolationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:CapabilityObjectiveRelationshipTypeVocab-1.0" => "nil",
    "maecVocabs:CommandandControlPropertiesVocab-1.0" => "nil",
    "maecVocabs:CommandandControlStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:CommandandControlTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:CommonCapabilityPropertiesVocab-1.0" => "nil",
    "maecVocabs:DNSActionNameVocab-1.0" => "nil",
    "maecVocabs:DataExfiltrationPropertiesVocab-1.0" => "nil",
    "maecVocabs:DataExfiltrationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:DataExfiltrationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:DataTheftPropertiesVocab-1.0" => "nil",
    "maecVocabs:DataTheftStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:DataTheftTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:DebuggingActionNameVocab-1.0" => "nil",
    "maecVocabs:DestructionPropertiesVocab-1.0" => "nil",
    "maecVocabs:DestructionStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:DestructionTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:DeviceDriverActionNameVocab-1.0" => "nil",
    "maecVocabs:DeviceDriverActionNameVocab-1.1" => "nil",
    "maecVocabs:DirectoryActionNameVocab-1.0" => "nil",
    "maecVocabs:DirectoryActionNameVocab-1.1" => "nil",
    "maecVocabs:DiskActionNameVocab-1.0" => "nil",
    "maecVocabs:DiskActionNameVocab-1.1" => "nil",
    "maecVocabs:FTPActionNameVocab-1.0" => "nil",
    "maecVocabs:FileActionNameVocab-1.0" => "nil",
    "maecVocabs:FileActionNameVocab-1.1" => "nil",
    "maecVocabs:FraudStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:FraudTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:GUIActionNameVocab-1.0" => "nil",
    "maecVocabs:GroupingRelationshipTypeVocab-1.0" => "nil",
    "maecVocabs:HTTPActionNameVocab-1.0" => "nil",
    "maecVocabs:HookingActionNameVocab-1.0" => "nil",
    "maecVocabs:HookingActionNameVocab-1.1" => "nil",
    "maecVocabs:IPCActionNameVocab-1.0" => "nil",
    "maecVocabs:IRCActionNameVocab-1.0" => "nil",
    "maecVocabs:ImportanceTypeVocab-1.0" => "nil",
    "maecVocabs:InfectionPropagationPropertiesVocab-1.0" => "nil",
    "maecVocabs:InfectionPropagationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:InfectionPropagationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:IntegrityViolationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:IntegrityViolationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:LibraryActionNameVocab-1.0" => "nil",
    "maecVocabs:LibraryActionNameVocab-1.1" => "nil",
    "maecVocabs:MachineAccessControlPropertiesVocab-1.0" => "nil",
    "maecVocabs:MachineAccessControlStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:MachineAccessControlTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:MalwareCapabilityVocab-1.0" => "nil",
    "maecVocabs:MalwareConfigurationParameterVocab-1.0" => "nil",
    "maecVocabs:MalwareDevelopmentToolVocab-1.0" => "nil",
    "maecVocabs:MalwareEntityTypeVocab-1.0" => "nil",
    "maecVocabs:MalwareLabelVocab-1.0" => "nil",
    "maecVocabs:MalwareSubjectRelationshipTypeVocab-1.0" => "nil",
    "maecVocabs:MalwareSubjectRelationshipTypeVocab-1.1" => "nil",
    "maecVocabs:NetworkActionNameVocab-1.0" => "nil",
    "maecVocabs:NetworkActionNameVocab-1.1" => "nil",
    "maecVocabs:NetworkShareActionNameVocab-1.0" => "nil",
    "maecVocabs:PersistencePropertiesVocab-1.0" => "nil",
    "maecVocabs:PersistenceStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:PersistenceTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:PrivilegeEscalationPropertiesVocab-1.0" => "nil",
    "maecVocabs:PrivilegeEscalationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:PrivilegeEscalationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:ProbingStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:ProbingTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:ProcessActionNameVocab-1.0" => "nil",
    "maecVocabs:ProcessMemoryActionNameVocab-1.0" => "nil",
    "maecVocabs:ProcessThreadActionNameVocab-1.0" => "nil",
    "maecVocabs:RegistryActionNameVocab-1.0" => "nil",
    "maecVocabs:RemoteMachineManipulationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:RemoteMachineManipulationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:SecondaryOperationPropertiesVocab-1.0" => "nil",
    "maecVocabs:SecondaryOperationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:SecondaryOperationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:SecurityDegradationPropertiesVocab-1.0" => "nil",
    "maecVocabs:SecurityDegradationStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:SecurityDegradationTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:ServiceActionNameVocab-1.0" => "nil",
    "maecVocabs:ServiceActionNameVocab-1.1" => "nil",
    "maecVocabs:SocketActionNameVocab-1.0" => "nil",
    "maecVocabs:SpyingStrategicObjectivesVocab-1.0" => "nil",
    "maecVocabs:SpyingTacticalObjectivesVocab-1.0" => "nil",
    "maecVocabs:SynchronizationActionNameVocab-1.0" => "nil",
    "maecVocabs:SystemActionNameVocab-1.0" => "nil",
    "maecVocabs:UserActionNameVocab-1.0" => "nil",
    "maecVocabs:UserActionNameVocab-1.1" => "nil"
}

$practices = {}

desc "Regenerate the data model documentation"
task :regenerate do
  # Make Liquid aware of the Jekyll includes directory
  #Liquid::Template.file_system = Liquid::LocalFileSystem.new("_includes")

  # Preload all versions of all schemas first so our introspection can tell what's available
  MaecSchemaSpy::Schema::VERSIONS.each {|v| MaecSchemaSpy::Schema.preload!(v)}

  MaecSchemaSpy::Schema::VERSIONS.each do |version|
    # Load the documentation page template
    template = File.read("_layouts/data_model_page.html")

    # Write the file for the data model autocompleter
    json = MaecSchemaSpy::Schema.all(version).map {|schema| schema.complex_types}.flatten.map {|type| {:name => type.name, :schema => type.schema.title, :link => type_link(type, version)}}
    File.open("js/autocomplete-#{version}.js", "w") {|f| f.write("window.typeSuggestions = " + JSON.dump(json))}

    # Iterate through all types in the schemas and create pages for them
    MaecSchemaSpy::Schema.all(version).each do |schema|
      schema.complex_types.each do |type|
        write_page(type, template, version)
      end
    end
  end
end

def write_page(type, template, version)
  destination = type_path(type, version)

  FileUtils.mkdir_p(destination)

  results = Liquid::Template.parse(template).render(
    'type' => {
      'latest_version' => MaecSchemaSpy::Schema.latest_version,
      'this_version' => version,
      'versions' => MaecSchemaSpy::Schema::VERSIONS.reject {|v|
        schema = MaecSchemaSpy::Schema.find(type.schema.prefix, v)
        (schema && schema.find_type(type.name)).nil?
      },
      'name' => type.name,
      'documentation' => process_documentation(type.documentation, version),
      'schema' => {
        'title' => type.schema.title,
        'prefix' => type.schema.prefix
      },
      'vocab?' => type.vocab?,
      'fields?' => type.fields.length > 0,
      'fields' => fields(type, version),
      'vocab_items' => vocab_items(type),
      'api_link' => python_link(type, version),
      'suggested_practices' => suggested_practices(type)
    }
  )

  File.open("#{destination}/index.html", "w") {|f| f.write(results)}
end

def type_link(type, version)
  "/#{type_path(type, version)}"
end

def type_path(type, version)
  "#{$destination}/#{version}/#{type.schema.prefix}/#{type.name}"
end

def python_link(type, version)
  prefix = ($maec_prefixes.include? type.prefix) ? $maec_uri : $cybox_uri
  link = $maec_links["#{type.schema.prefix}:#{type.name}"]
  if link then
    prefix + link
  else
    nil
  end
end

def suggested_practices(type)
  $practices["#{type.schema.prefix}:#{type.name}"]
end

def fields(type, version)
  type.fields.map do |field|
    {
      'name' => field.name,
      'link' => (field.type.kind_of?(MaecSchemaSpy::ComplexType) && field.type.schema && !field.type.schema.blacklisted?) ? type_link(field.type, version) : false,
      'type' => field.type.name,
      'documentation' => process_documentation(field.documentation.split("\n"), version),
      'occurrence' => field_occurrence(field)
    }
  end
end

def field_occurrence(field)
  if field.kind_of?(MaecSchemaSpy::Attribute)
    field.use
  else
    max_occurs = field.max_occurs == 'unbounded' ? 'n' : field.max_occurs
    "#{field.min_occurs}..#{max_occurs}"
  end
end

def vocab_items(type)
  return [] unless type.vocab?

  type.vocab_values.map {|v|
    {
      'name' => v[0],
      'description' => v[1]
    }
  }
end

def process_documentation(docs, version)
  if docs.kind_of?(String)
    add_internal_links(docs, version)
  else
    docs.map {|doc|
      add_internal_links(doc, version)
    }
  end
end

def add_internal_links(doc, version)
  doc
    .gsub(/\S+Vocab-\d(\.\d){1,2}/) {|match| "<a href='/#{$destination}/#{version}/maecVocabs/#{match}'>#{match}</a>"}
    .gsub(/ \S+Type /) do |match|
      name = match.strip
      type = find_type(name)
      if type
        " <a href='#{type_link(type, version)}'>#{name}</a> "
      else
        match
      end
    end
end

def find_type(type)
  types = MaecSchemaSpy::Schema.all.map do |schema|
    schema.find_type(type)
  end.compact

  # Only return the found type if we found exactly one, otherwise it's ambiguous
  types.length == 1 ? types.first : nil
end
