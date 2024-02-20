#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let n = 0;

    data.results.forEach((film) => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18')) {
        n++;
      }
    });
    console.log(n);
  }
});
