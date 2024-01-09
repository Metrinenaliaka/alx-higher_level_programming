#!/usr/bin/node
/*
creates sorted dictionary or lists of occurences
*/
const dict = require('./101-data.js').dict;

const newDict = {};

for (const key in dict) {
  newDict[dict[key]] = [];
}

for (const key in dict) {
  newDict[dict[key]].push(key);
}

console.log(newDict);
