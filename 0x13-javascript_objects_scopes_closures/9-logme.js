#!/usr/bin/node

let counter = 0;
exports.logMe = function (item) {
  const str = `${counter}: ${item}`;
  console.log(str);
  counter++;
};
