#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const filecontent = process.argv[3];

fs.writeFile(filepath, filecontent, (err) => {
  if (err) throw err;
    console.log(err);
});