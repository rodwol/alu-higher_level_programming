#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // define a constructor
  constructor (size) {
    // Call the constructor of Rectangle with width and height as size
    super(size, size);
  }
}

module.exports = Square;
