fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then(resp => {
    return resp.json();
  })
  .then(movies => {
    movies.results.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }); // alx-task
