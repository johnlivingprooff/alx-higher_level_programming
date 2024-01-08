#!/usr/bin/node
const myStr = 'C is fun';
const arg = process.argv.slice(2);
let i = 0;

if (!isNaN(parseInt(arg[0]))) {
  while (i < parseInt(arg)) {
    console.log(myStr);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
