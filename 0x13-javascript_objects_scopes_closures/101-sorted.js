#!/usr/bin/node

var dict = require('./101-data.js').dict;

var newDict = {};

for (const key in dict) {
  if (dict[key] in dict) continue;
  else newDict[dict[key]] = [];
}

for (const key in dict) {
  var newKey = dict[key];
  newDict[newKey].push(key);
}

console.log(newDict);
