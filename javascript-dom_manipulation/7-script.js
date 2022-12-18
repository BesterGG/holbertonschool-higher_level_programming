fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movies_list = document.querySelector('#list_movies');
    for (const movie of data.results) {
      const li = document.createElement('li');
      li.innerHTML = movie.title;
      movies_list.appendChild(li);
    }
  });