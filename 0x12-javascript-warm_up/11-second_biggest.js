#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs.length === 0) {
    console.log(1);
} else {
    let max = 0, i;
    for (i = 0; i < myArgs.length; i++) {
        if (parseInt(myArgs[i]) > max) {
            max = parseInt(myArgs[i]);
        }
    }
    console.log(max);
}
