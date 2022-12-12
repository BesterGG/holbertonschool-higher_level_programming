#!/usr/bin/node
const SQ = require('./5-square');
class Square extends (SQ) {
  charPrint (C) {
    let row = '';
    let col = 0;
    while (col < this.width) {
      if (C) {
        row += C;
        col++;
      } else {
        row += 'X';
        col++;
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Square;
