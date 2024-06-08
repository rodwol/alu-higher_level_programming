#!/usr/bin/node

$(document).ready(function() {
    // URL of the API to fetch data from
    var apiURL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Perform an HTTP GET request using jQuery's $.get() method
    $.get(apiURL, function(data) {
        // Extract the movie titles from the data received
        var movies = data.results;

        // Iterate over each movie and create a new <li> element for each title
        movies.forEach(function(movie) {
            // Create a new <li> element and set its text to the movie title
            var listItem = $('<li>').text(movie.title);

            // Append the new <li> element to the <ul id="list_movies">
            $('#list_movies').append(listItem);
        });
    });
});