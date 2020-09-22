#!/usr/bin/node

const url = process.argv[2];

const request = require('request');

request(url, function (error, response, body) {
  if (error) return console.error(error);
  if (response.statusCode !== 200) return;
  const data = JSON.parse(body);
  let results = data.results;
  if (results === undefined) results = [data];
  let counter = 0;
  const charId = 'https://swapi-api.hbtn.io/api/people/18/';
  for (const i in results) {
    const people = results[i].characters;
    if (people.includes(charId)) counter++;
  }
  console.log(counter);
});
