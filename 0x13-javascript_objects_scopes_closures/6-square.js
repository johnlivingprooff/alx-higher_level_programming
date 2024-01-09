#!/usr/bin/node
const _Square = require('./5-square');

class Square extends _Square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      let j = 0;
      let row = '';
      while (j < this.width) {
        row += c;
        j++;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
