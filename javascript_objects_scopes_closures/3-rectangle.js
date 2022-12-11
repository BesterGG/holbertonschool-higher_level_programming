#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      let row = '';
      let col = 0;
  
      // Build a row of X characters
      while (col < this.width) {
        row += 'X';
        col++;
      }
  
      // Print the rows
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
  
module.exports = Rectangle;
