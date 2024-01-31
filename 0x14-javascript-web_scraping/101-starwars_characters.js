#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
