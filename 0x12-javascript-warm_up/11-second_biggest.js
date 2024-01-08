#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments */
'use strict';
if ((process.argv.length <= 3)) {
  console.log(0);
} else {
  let numArray = [];
  for (let i = 2; i < process.argv.length; i++) {
    numArray.push(parseInt(process.argv[i]));
    numArray = numArray.sort();
  }
  numArray.reverse();
  console.log(numArray[1]);
}
