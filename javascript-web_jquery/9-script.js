#!/usr/bin/node

$(document).ready(function() {
    // URL of the API to fetch data from
    var apiURL = 'https://fourtonfish.com/hellosalut/?lang=fr';

    // Perform an HTTP GET request using jQuery's $.get() method
    $.get(apiURL, function(data) {
        // Extract the 'hello' value from the data received
        var helloText = data.hello;

        // Update the content of the <div id="hello"> with the 'hello' value
        $('#hello').text(helloText);
    });
});
