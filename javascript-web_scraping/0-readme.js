#!/usr/bin/node

const fs = require('fs');

// Get the file path from the first argument
const filepath = process.argv[2];

// Read the file content in utf-8 encodingfs
fs.readFile(filepath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
