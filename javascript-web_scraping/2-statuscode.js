#!/usr/bin/node

const request = require('request');

// Get the URL from command-line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
