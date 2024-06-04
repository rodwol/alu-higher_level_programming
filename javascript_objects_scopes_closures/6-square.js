#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  // Instance method to print the square with a specified character
  charPrint (c) {
    const char = c || 'X'; // use 'X' if c is undefined
    if (this.width && this.height) {
      const row = char.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
