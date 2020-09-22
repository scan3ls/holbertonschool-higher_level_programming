#!/usr/bin/node

const args = process.argv;
const url = args.slice(2)[0];
const filePath = args.slice(2)[1];

const fs = require('fs');
const request = require('request');

request(url, function (error, response, body) {
  if (error) console.error(error);
  const writeString = body;
  fs.writeFile(filePath, writeString, { encoding: 'utf-8' }, function (err) {
    if (err) {
      throw err;
    }
  });
});
