#!/usr/bin/node
const square = 'X';
const arg = process.argv.slice(2);
let i = 0;

if (!isNaN(parseInt(arg[0]))) {
  while (i < parseInt(arg[0])) {
    let row = '';
    let j = 0;
    while (j < parseInt(arg[0])) {
      row += square;
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
