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
    const promises = [];

    characters.forEach(characterUrl => {
      // Create a promise for each character request
      const promise = new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
      promises.push(promise);
    });

    // Wait for all promises to resolve
    Promise.all(promises)
      .then(characterNames => {
        // Print character names in order
        characterNames.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.error(error);
      });
  }
});
