#!/usr/bin/node
const argv = process.argv;
add(Number(argv[2]), Number(argv[3]));
function add (a, b) {
  console.log(a + b);
}
