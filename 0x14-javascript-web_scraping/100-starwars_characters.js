#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    const characters = results.characters;
    for (let j = 0; j < characters.length; j++) {
      const peopleUrl = characters[j];
      request(peopleUrl, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
