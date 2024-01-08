#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv.slice(2);

if (!isNaN(parseInt(arg[0])) && parseInt(arg[0]) >= 0) {
  const result = factorial(parseInt(arg[0]));
  console.log(result);
} else if (isNaN(parseInt(arg[0]))) {
  console.log(1);
}
