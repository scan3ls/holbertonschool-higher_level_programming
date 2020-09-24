const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const name = '';

$(function () {
  $.get(url, function (data, textStatus) {
    // name = data.name;
    const films = data.results;
    for (const i in films) {
      const title = films[i].title;
      $('UL#list_movies').append(`<li>${title}</li>`);
    }
    console.log(data);
  });
});

$('HEADER').click(function () {
  $('DIV#character').text(name);
});
