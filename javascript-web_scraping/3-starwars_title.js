#!/usr/bin/node

const request = require('request');

// Get the movie ID from command-line arguments
const movieID = process.argv[2];

// Construct the URL with the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API endpoint
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
