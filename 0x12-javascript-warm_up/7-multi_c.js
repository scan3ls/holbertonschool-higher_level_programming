#!/usr/bin/node

const x = process.argv[2];
const str = 'C is fun';
let i;
if (x === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log(str);
  }
}