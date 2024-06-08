#!/usr/bin/node

$(document).ready(function() {
    // Add a click event listener to the div#red_header
    $('#red_header').click(function() {
        // Add the 'red' class to the header element
        $('header').addClass('red');
    });
});
