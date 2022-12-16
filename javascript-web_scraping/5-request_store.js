#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
