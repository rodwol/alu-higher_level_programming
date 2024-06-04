#!/usr/bin/node

class Rectangle {
  // define a constructor
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // create an empty object
      this.width = undefined;
      this.height =  undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
