#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

const a = Number(args[0]); const b = Number(args[1]);
const sumH = add(a, b);
console.log(sumH);
