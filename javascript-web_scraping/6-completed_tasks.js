#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const all = JSON.parse(body);
    const tk = {};
    for (const key of all) {
      if (key.completed) {
        const uid = key.userId;
        if (!tk[uid]) {
          tk[uid] = 1;
        } else {
          tk[uid] += 1;
        }
      }
    }
    console.log(tk);
  }
});
