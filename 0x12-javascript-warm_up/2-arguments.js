#!/usr/bin/node
/**
 *  prints a message depending of the number of arguments passed
 */
'use strict';
const args = process.argv.length;
if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
