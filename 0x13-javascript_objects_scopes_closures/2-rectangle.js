#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
