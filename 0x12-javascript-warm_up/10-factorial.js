#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = factorial(num1);
console.log(num2);
