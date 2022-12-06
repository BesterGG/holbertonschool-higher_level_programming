#!/usr/bin/node

const argv = process.argv.sort();
const large = argv.length;
let i;
let top = 0;
let second = 0;

for (i = 0; i < large; i++) {
  if (Number(argv[i]) > top) {
    top = Number(argv[i]);
  }
}
for (i = 0; i < large; i++) {
  if (Number(argv[i]) > second && Number(argv[i]) < top) {
    second = Number(argv[i]);
  }
}
console.log(second);
