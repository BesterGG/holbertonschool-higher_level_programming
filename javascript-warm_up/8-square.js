#!/usr/bin/node
const argv = process.argv;
const num = Number(argv[2]);
const val = isNaN(num);
let i, j;
if (typeof num === 'number' && val === false) {
  for (i = 0; i < num; i++) {
    let row = '';
    for (j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
