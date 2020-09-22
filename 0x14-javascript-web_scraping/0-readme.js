#!/usr/bin/node

const args = process.argv;
const filePath = args.slice(2)[0];
const fs = require('fs');
fs.readFile(filePath, { encoding: 'utf-8' }, function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
