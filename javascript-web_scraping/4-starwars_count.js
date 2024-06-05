#!/usr/bin/node

const request = require('request');

// Get the API URL from command-line arguments
const url = process.argv[2];

// Character ID for Wedge Antilles
const charID = 18;

// Make a GET request to the Star Wars API endpoint to fetch all films
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    // Initialize a counter for the number of movies where Wedge Antilles is present
    let count = 0;
    // Iterate through each film
    films.forEach(film => {
      // Check if Wedge Antilles is present in the list of characters for the current film
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charID}/`)) {
        count++;
      }
    });
    console.log(count);
  }
});
