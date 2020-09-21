#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'string') {
      this.print(c);
    } else {
      this.print('X');
    }
  }

  print (c) {
    let str = '';
    if (typeof c === 'string') {
      str = c;
    } else {
      str = 'X';
    }

    let baseStr = '';
    for (let i = 0; i < this.width; i++) {
      baseStr = baseStr + str;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(baseStr);
    }
  }
};
