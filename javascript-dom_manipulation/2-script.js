#!/usr/bin/node
const header = document.querySelector('header');
header.addEventListener('click', function () {
  header.classList.add('red');
});
