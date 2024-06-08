#!/usr/bin/node

$(document).ready(function() {
    // Add a click event listener to the div#toggle_header
    $('#toggle_header').click(function() {
        // Check the current class of the header element
        var currentClass = $('header').attr('class');

        // Toggle class between 'red' and 'green'
        if (currentClass === 'red') {
            $('header').removeClass('red').addClass('green');
        } else if (currentClass === 'green') {
            $('header').removeClass('green').addClass('red');
        }
    });
});
