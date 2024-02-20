#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const dataStr = process.argv[3];

fs.writeFile(filePath, dataStr, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
