#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return a + b;
  }
}

const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);
const num3 = add(num1, num2);

console.log(num3);
