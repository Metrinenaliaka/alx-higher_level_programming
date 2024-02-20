#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.
*/
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      const task = json[i];
      if (task.completed === true) {
        if (results[task.userId] !== undefined) {
          results[task.userId] += 1;
        } else {
          results[task.userId] = 1;
        }
      }
    }
    console.log(results);
  }
});
