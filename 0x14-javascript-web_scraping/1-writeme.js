#!/usr/bin/node

const args = process.argv;
const filePath = args.slice(2)[0];
const writeString = args.slice(2)[1];

const fs = require('fs');

fs.writeFile(filePath, writeString, { encoding: 'utf-8' }, function (err) {
  if (err) {
    throw err;
  }
});
