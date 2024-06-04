const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

function getCharacterNames(characters, index = 0) {
  if (index === characters.length) {
    return;
  }

  request({ url: characters[index], json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }

    console.log(body.name);
    getCharacterNames(characters, index + 1);
  });
}

request({ url, json: true }, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  const characters = body.characters;
  getCharacterNames(characters);
});

