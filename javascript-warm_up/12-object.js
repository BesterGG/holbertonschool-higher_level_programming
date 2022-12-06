#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// const update_value = Object.assign(myObject, {type: 'object', value: 89});
myObject.value = 89;
console.log(myObject);
