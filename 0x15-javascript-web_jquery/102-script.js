$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
      .then(resp => {
        return resp.json();
      })
      .then(langs => {
        $('#hello').text(langs.hello);
      });
  });
});
