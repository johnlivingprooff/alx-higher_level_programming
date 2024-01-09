#!/usr/bin/node
const fileSource = require('fileSource');
const first = fileSource.readFileSync(process.argv[2]).toString();
const second = fileSource.readFileSync(process.argv[3]).toString();
fileSource.writeFileSync(process.argv[4], first + second);
