#!/usr/bin/node
/**
 * script that prints the first argument passed to it
 */
'use strict';
const args = process.argv.length;
if (args < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
