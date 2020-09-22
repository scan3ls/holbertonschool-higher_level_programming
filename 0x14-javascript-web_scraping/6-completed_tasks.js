#!/usr/bin/node

const url = process.argv[2];

const request = require('request');

request(url, function (error, response, body) {
  if (error) return console.error(error);
  if (response.statusCode !== 200) return;
  const obj = JSON.parse(body);
  const counter = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };

  if (obj.length === undefined) {
    if (obj.completed) counter[obj.userId]++;
    console.log(counter);
    return;
  }

  for (let i = 0; i < obj.length; i++) {
    const current = obj[i];
    const userId = current.userId;
    const completed = current.completed;
    if (completed) {
      counter[userId.toString()]++;
    }
  }
  console.log(counter);
});
