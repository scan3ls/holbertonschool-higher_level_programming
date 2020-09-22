#!/usr/bin/node

const args = process.argv;
const url = args.slice(2)[0];

const request = require('request');

request(url, function (error, response, body) {
  if (error) console.error(error);
  console.log('code:', response && response.statusCode);
  // console.log('body:', body);
});
