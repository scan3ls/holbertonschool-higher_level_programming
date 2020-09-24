const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
const name = '';

$(function () {
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
    // console.log(data);
  });
});

$('header').click(function () {
  $('DIV#character').text(name);
});
