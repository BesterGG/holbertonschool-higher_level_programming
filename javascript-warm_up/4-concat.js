#!/usr/bin/node
const argv = process.argv;
const str1 = argv[2];
const str2 = argv[3];
if (!argv[2] & !argv[3]) {
  console.log('undefined is undefined');
} else {
console.log(str1.concat(' is ', str2));
}