#!/usr/bin/node
const request = require('request');
const filmid = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmid}`;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
