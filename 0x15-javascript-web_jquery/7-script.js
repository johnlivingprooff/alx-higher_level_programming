fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    $('#character').text(data.name);
  });
