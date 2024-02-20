#!/usr/bin/node
/*
script that gets the contents of a webpage and stores it in a file.
*/
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const content = body;
    fs.writeFile(file, content, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
