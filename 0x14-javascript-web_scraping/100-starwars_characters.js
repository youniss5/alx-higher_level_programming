#!/usr/bin/node

const id = process.argv[2];
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(id + url, function (error, res, body) {
  if (error) {
    console.log(error);
 }
  const data = JSON.parse(body);
  const aa = data.characters;
  for (const x of aa) {
    req.get(x, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
