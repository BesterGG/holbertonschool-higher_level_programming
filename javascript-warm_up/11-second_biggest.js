#!/usr/bin/node

const argv = process.argv.sort();
const large = argv.length
let i, top = 0, second = 0;

for (i = 0;i < large;i++) {
  if (argv[i] > top){
      top = argv[i];
}
}
for (i = 0;i < large;i++) {
  if (argv[i] > second && argv[i] < top){
    second = argv[i];  
  }
}
console.log(second);
