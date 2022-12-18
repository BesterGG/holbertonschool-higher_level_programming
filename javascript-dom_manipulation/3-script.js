#!/usr/bin/node
const header = document.querySelector('header');
const toggle = document.querySelector('#toggle_header');
toggle.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
