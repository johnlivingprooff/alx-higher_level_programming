#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs.length === 0) {
  console.log(1);
} else {
  let max = parseInt(myArgs[0]); // Initialize max with the first argument
  for (let i = 1; i < myArgs.length; i++) {
    const currentValue = parseInt(myArgs[i]);
    if (!isNaN(currentValue) && currentValue > max) {
      max = currentValue;
    }
  }
  console.log(max);
}
