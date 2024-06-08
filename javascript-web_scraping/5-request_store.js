#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the url and path of the file to store the contents from command-line arguments
const url = process.argv[2];
const filepath = process.argv[3];

// transfer the content to the file in utf-8 encoding
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filepath, body, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
