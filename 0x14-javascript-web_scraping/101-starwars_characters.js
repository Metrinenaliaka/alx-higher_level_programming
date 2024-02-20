#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    const characters = results.characters;
    const promises = [];
    for (let j = 0; j < characters.length; j++) {
      promises.push(new Promise((resolve, reject) => {
        const peopleUrl = characters[j];
        request.get(peopleUrl, function (err, res, body) {
          if (err) {
            reject(err);
          } else {
            const person = JSON.parse(body);
            resolve(person.name);
          }
        });
      }));
    }
    Promise.all(promises).then((names) => names.forEach((name) => console.log(name)));
  }
});
