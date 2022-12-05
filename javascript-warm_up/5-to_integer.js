#!/usr/bin/node
const argv = process.argv;
const num = Number(argv[2]);
let val = isNaN(num);
if (typeof num === 'number' && val === false) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
