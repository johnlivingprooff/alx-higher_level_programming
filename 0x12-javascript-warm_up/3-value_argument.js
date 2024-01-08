#!/usr/bin/node
// prints the first argument passed to it
const argv = process.argv.slice(2);
const argl = process.argv.length - 1;

if (argl <= 1) {
  console.log('No argument');
} else if (argl >= 2) {
  console.log(argv[0]);
}
