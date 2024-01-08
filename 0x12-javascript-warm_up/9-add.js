#!/usr/bin/node
/*
 * script that prints the addition of 2 integers
 */
const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);
function add (a, b) {
  return (a + b);
}
console.log(add(num1, num2));
