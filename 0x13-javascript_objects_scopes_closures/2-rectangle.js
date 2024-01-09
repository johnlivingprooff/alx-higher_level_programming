#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
        return;
    } else {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;
