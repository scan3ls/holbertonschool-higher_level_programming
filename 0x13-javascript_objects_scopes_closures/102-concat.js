#!/usr/bin/node

const pathOne = process.argv[2];
const pathTwo = process.argv[3];
const pathThree = process.argv[4];

const fs = require('fs');
const { exit } = require('process');

if (pathOne === undefined || pathTwo === undefined || pathThree === undefined) exit();

fs.readFile(pathOne, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(pathThree, data, err => {
    if (err) {
      console.error(err);
    }
  });
});

fs.readFile(pathTwo, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }

  fs.appendFile(pathThree, data, err => {
    if (err) {
      console.error(err);
    }
  });
});
