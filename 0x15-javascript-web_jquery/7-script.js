const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
let name = '';

$(function () {
  $.get(url, function (data, textStatus) {
    name = data.name;
    // console.log(data);
  });
});

$('HEADER').click(function () {
  $('DIV#character').text(name);
});
