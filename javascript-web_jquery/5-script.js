#!/usr/bin/node

$(document).ready(function() {
    // Add a click event listener to the div#add_item
    $('#add_item').click(function() {
        // Create a new <li> element
        var newItem = $('<li>').text('Item');

        // Append the new <li> element to the <ul> element with class my_list
        $('.my_list').append(newItem);
    });
});
