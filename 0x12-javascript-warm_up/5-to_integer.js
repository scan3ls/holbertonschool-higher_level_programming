#!/usr/bin/node

const args = process.argv;
const arg1 = args[2];

const num1 = parseInt(arg1);

if (isNaN(num1)) {
  console.log('Not a number');
} else {
  console.log('My number: ', num1);
}
