#!/usr/bin/node

$(document).ready(function() {
    // Add a click event listener to the div#update_header
    $('#update_header').click(function() {
        // Update the text content of the header element
        $('header').text('New Header!!!');
    });
});