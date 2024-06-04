#!/usr/bin/node

class Rectangle {
  // define a constructor (special method in a class that is called when an instance of the class is created)
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // create an empty object
      return;
    }
    this.width = w;
    this.height = h;
  }

  // Instance method to print the rectangle
  print () {
    if (this.width && this.height) {
      const row = 'X'.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }

  // Instance method to rotate the rectangle
  rotate () {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  // Instance method to double the dimensions of the rectangle
  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
