#!/usr/bin/node

const args = process.argv;
const numbers = args.splice(2);
let i, num;
let first = -Infinity;
let second = -Infinity;

for (i = 0; i < numbers.length; i++) {
  num = parseInt(numbers[i]);
  if (num > first) {
    second = first;
    first = num;
  } else if (num > second) {
    second = num;
  }
}

if (second === -Infinity){
  second = 0;
}

console.log(second)
