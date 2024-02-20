#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
