#!/usr/bin/node

const args = process.argv;
const numbers = args.splice(2);
const second = numbers.sort().reverse()[1];

if (isNaN(parseInt(second))) {
  console.log(0);
} else {
  console.log(second);
}
