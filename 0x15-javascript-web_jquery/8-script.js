$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const films = data.results;
    for (let i = 0; i < films.length; i++) {
      $('UL#list_movies').append('<li>' + films[i].title + '</li>');
    }
  });
});
