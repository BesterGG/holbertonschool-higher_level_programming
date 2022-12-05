#!/usr/bin/node
const myArgs = process.argv;
const len = myArgs.length - 1;

if (len > 1 & len < 2) {
    console.log('Argument found');
} else if (len > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
