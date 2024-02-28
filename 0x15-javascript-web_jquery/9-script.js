fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(resp => {
    return resp.json();
  })
  .then(lang => {
    $('#hello').text(lang.hello);
  });
