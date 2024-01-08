#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  let max = parseInt(myArgs[0]); // Initialize max with the first argument
  let secondMax = parseInt(myArgs[1]);
  if (secondMax > max) {
    [max, secondMax] = [secondMax, max];
  }

  for (let i = 2; i < myArgs.length; i++) {
    const currentValue = parseInt(myArgs[i]);
    if (!isNaN(currentValue)) {
      if (currentValue > max) {
        secondMax = max;
        max = currentValue;
      } else if (currentValue > secondMax && currentValue !== max) {
        secondMax = currentValue;
      }
    }
  }
  console.log(secondMax);
}
