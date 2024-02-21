#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) return console.error(error);

  const data = JSON.parse(body);
  let count = 0;

  data.results.forEach(film => {
    const filmChar = film.characters;
    filmChar.forEach(char => {
      if (char.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
