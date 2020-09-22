#!/usr/bin/node

const url = process.argv[2];

const request = require('request');

request(url, function (error, response, body) {
  if (error) return console.error(error);
  if (response.statusCode !== 200) return;
  const obj = JSON.parse(body);
  const counter = {};

  if (obj.length === undefined) {
    if (obj.completed) {
      if (counter[obj.userId] === undefined) counter[obj.userId] = 1;
      else counter[obj.userId]++;
    }
    console.log(counter);
    return;
  }

  for (let i = 0; i < obj.length; i++) {
    const current = obj[i];
    const userId = current.userId;
    const completed = current.completed;
    if (completed) {
      if (counter[userId] === undefined) counter[userId] = 1;
      else counter[userId]++;
    }
  }
  console.log(counter);
});
