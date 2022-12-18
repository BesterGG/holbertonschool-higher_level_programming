#!/usr/bin/node
const add_item = document.getElementById('add_item');
add_item.addEventListener('click', () => {
  const newli = document.createElement('li');
  newli.innerHTML = 'Item';
  const list = document.querySelector('.my_list');
  list.appendChild(newli);
});
