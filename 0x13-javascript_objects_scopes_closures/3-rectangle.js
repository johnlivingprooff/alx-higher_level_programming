#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (Number.isInteger(w) && w > 0 && h > 0 && Number.isInteger(h)) {
        this.width = w;
        this.height = h;
      }
    }
    print() {
        let x = 'X';
        for (let i = 0; i < this.height; i++) {
            let j = 0;
            let row = '';
            while (j < this.width) {
                row += x;
                j++;
            }
            console.log(row);
        }
    }
  }
  
  module.exports = Rectangle;
  