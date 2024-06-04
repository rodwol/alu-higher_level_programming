#!/usr/bin/node

class Rectangle {
  // define a constructor
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if width or height is not a positive integer or is zero

    }
  }
}

module.exports = Rectangle;
