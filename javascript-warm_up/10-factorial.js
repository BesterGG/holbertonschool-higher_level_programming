#!/usr/bin/node
const argv = process.argv;
const val = isNaN(argv[2]);
factorial(Number(argv[2]));

function factorial (a) {
  let res = 1;
  if (val === true || !a) {
    console.log('1');
  } else if (a < 0) {
    console.log('-1');
  } else if (a > 0) {
    for (let i = 1; i <= a; i++) {
      res *= i;
    }
    console.log(res);
  }
}
