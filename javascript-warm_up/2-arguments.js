#!/usr/bin/node
const myArgs = process.argv
let len = myArgs.length - 1

if (len > 1){
    console.log('Argument found');
} else {
    console.log('No argument');
}