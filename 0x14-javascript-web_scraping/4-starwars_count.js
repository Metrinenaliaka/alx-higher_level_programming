#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
