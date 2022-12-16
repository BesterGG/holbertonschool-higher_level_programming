#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const v of data) {
      for (const i of v.characters) {
        if (i === 'https://swapi-api.hbtn.io/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
