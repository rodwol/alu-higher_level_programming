#!/usr/bin/node

const fs = require('fs');

// Get the file path and the string to write from command-line arguments
const filepath = process.argv[2];
const content = process.argv[3];

// Write the content to the file in utf-8 encoding
fs.writeFile(filepath, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
