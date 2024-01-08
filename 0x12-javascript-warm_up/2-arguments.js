#!/usr/bin/node
const args = process.argv.length - 1;

if (args <= 1) {
  console.log('No argument');
} else if (args === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
