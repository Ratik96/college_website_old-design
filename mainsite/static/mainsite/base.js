$(document).ready(function (){
  // Create a select and append to #menu
  var $select = $('<select></select>');
  $('nav').append($select);

  // Cycle over menu links
  $('nav a').each(function (){
    var $anchor = $(this);
    // Create an option
    var $option = $('<option></option>');

    // Deal with 'selected' class addition
    if ($anchor.parent().hasClass('selected')) {
      $option.prop('selected', true);
    }
    // Option's value is the href's link
    $option.val($anchor.attr('href'));
    // Option's text is the text of the link
    $option.text($anchor.text());
    // Append option to select
    $select.append($option);

  });

  // Adding a slight margin-top to the select
  $select.css('margin-top', '20px');

  // Bind change listener to the select
  $select.change(function(){
    // Go to the select's location
    window.location = $select.val();
  });
});