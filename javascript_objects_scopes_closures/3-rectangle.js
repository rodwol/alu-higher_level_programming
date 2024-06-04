#!/usr/bin/node

class Rectangle {
  // define a constructor
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // create an empty object
    }
    this.width = w;
    this.height = h;
  }

  // creating an instance method to print the rectangle
  print () {
    if (this.width && this.height) {
      const row = 'X'.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Rectangle;
