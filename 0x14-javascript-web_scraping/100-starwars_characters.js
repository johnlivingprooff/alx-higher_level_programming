#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);

    data.characters.forEach(character => {
      request.get(character, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const charName = JSON.parse(body);
          console.log(charName.name);
        }
      });
    });
  }
});
