var typeSuggestor = new Bloodhound({
  datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.name)},
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: window.typeSuggestions,
  limit: 10,
  sorter: function(a, b) {
    return a.name.length - b.name.length;
  }
});

typeSuggestor.initialize();

$('.doc-types').typeahead({
  minLength: 3,
  highlight: true,
  autoselect: true
},
{
  source: typeSuggestor.ttAdapter(),
  displayKey: 'name',
  templates: {
    suggestion: function(suggestion) {
      return "<p>" + suggestion.name + "<span class='subdued'>" + suggestion.schema + "</span></p>"
    }
  }
});

$('.doc-types').on('typeahead:selected', function(evt, suggestion) {
  document.location.href = window.location.protocol + "//" + window.location.host + suggestion.link;
});

$('#nav-version select').on('change', function() {
  var oldLocation = document.location.href;
  var newLocation = oldLocation.replace(/data-model\/[^\/]+\//, "data-model/" + $(this).val() + "/");
  document.location.href = newLocation;
});

$('table').addClass('table'); // Makes all tables bootstrap tables

$(document).ready(function() {
    $('.dropdown-toggle').dropdown()
    $('.coming-soon').tooltip()
    $('.idiom-construct').tooltip()
});