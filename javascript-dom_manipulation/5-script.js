#!/usr/bin/node
const header = document.querySelector('header');
const updateheader = document.querySelector('#update_header');
updateheader.addEventListener('click', () => {
  header.textContent = 'New Header!!!'; //Se puede hacer con innerhtml pero 
  //ejecutaria codigo html
});
