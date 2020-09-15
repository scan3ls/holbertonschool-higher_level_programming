#!/usr/bin/node

const args = process.argv;
const arg1 = args[2];
const num1 = parseInt(arg1);
let str = '';
let x;
let y;

if (isNaN(num1)) {
  console.log('Missing size');
} else {
  for (x = 0; x < num1; x++) {
    str = str.concat('', 'X');
  }
  for (y = 0; y < num1; y++) {
    console.log(str);
  }
}
