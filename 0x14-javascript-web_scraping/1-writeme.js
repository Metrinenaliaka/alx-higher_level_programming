#!/usr/bin/node
/*
reads a file and prints the contents
*/
const fs = require('fs');

const file = process.argv[2];
const content = process.argv[3];

fs.writeFile(file, content, function (err) {
  if (err) {
    console.log(err);
  }
});
