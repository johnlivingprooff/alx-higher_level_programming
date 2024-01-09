#!/usr/bin/node
const dict = require('./101-data').dict;
const myDict = {};

for (const uID in dict) {
    const occurances = dict[uID];
    if (occurances in myDict) {
        myDict[occurances].push(uID);
    } else {
        myDict[occurances] = [uID];
    }
}

console.log(myDict);
