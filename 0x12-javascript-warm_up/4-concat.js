#!/usr/bin/node

const args = process.argv;
let str1 = args[2];
let str2 = args[3];

if (str1 === undefined) {
  str1 = 'undefined';
}
if (str2 === undefined) {
  str2 = 'undefined';
}

console.log(str1.concat(' is ', str2));
