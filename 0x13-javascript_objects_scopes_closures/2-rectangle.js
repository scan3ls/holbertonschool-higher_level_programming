#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) {

    } else if (w <= 0 || h <= 0) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
};
