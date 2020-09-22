#!/usr/bin/node

const args = process.argv;
const movieNumber = args.slice(2)[0];
const url = `https://swapi-api.hbtn.io/api/films/${movieNumber}`;

const request = require('request');

request(url, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  console.log(data.title);
});
