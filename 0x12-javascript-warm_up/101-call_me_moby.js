#!/usr/bin/node
function myFunc(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { myFunc };
