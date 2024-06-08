#!/usr/bin/node

$(document).ready(function() {
    // URL of the API to fetch data from
    var apiURL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    // Perform an HTTP GET request using jQuery's $.get() method
    $.get(apiURL, function(data) {
        // Extract the character name from the data received
        var characterName = data.name;

        // Update the content of the <div id="character"> with the character name
        $('#character').text(characterName);
    });
});