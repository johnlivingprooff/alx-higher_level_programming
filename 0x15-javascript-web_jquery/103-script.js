$(document).ready(function () {
    function translate() {
      const lang = $('#language_code').val();
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
        .then(resp => {
          return resp.json();
        })
        .then(langs => {
          $('#hello').text(langs.hello);
        });
    }

    $('#btn_translate').click(function () {
        translate();
    });

    $('#language_code').keypress(function (event) {
        if (event.key === 'Enter') {
            translate();
        }
    });
  });
  