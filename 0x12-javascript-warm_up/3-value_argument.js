#!/usr/bin/node
// prints the first argument passed to it
const argv = process.argv.slice(2);
const arg_l = process.argv.length - 1;

if (arg_l <= 1) {
  console.log('No argument');
} else if (arg_l >= 2) {
  console.log(argv[0]);
}
