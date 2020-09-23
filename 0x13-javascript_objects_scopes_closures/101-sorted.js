#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

for (const key in dict) {
  if (dict[key] in newDict) continue;
  else newDict[dict[key]] = [];
}

for (const key in dict) {
  const newKey = dict[key];
  //console.log(newDict[newKey])
  newDict[newKey].push(key);
}

console.log(newDict);
