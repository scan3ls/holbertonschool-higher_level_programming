#!/usr/bin/node

const url = process.argv[2];

const request = require('request');

request(url, function (error, response, body) {
  if (error) return console.error(error);
  const data = JSON.parse(body);
  const results = data.results;
  let counter = 0;
  const charId = 'https://swapi-api.hbtn.io/api/people/18/';
  for (let i = 0; i < results.length; i++) {
    const people = results[i].characters;
    if (people.includes(charId)) counter++;
  }
  console.log(counter);
});
