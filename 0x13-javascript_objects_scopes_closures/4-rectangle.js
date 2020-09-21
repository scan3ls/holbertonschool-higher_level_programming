#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) {
      this.width = 0;
      this.height = 0;
    } else if (w <= 0 || h <= 0) {
      this.width = 0;
      this.height = 0;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let baseStr = '';
    for (let i = 0; i < this.width; i++) {
      baseStr = baseStr + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(baseStr);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
