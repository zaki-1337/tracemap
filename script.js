'use strict';

const form = document.querySelector('.hosts');

const map = L.map('map').setView([36, 40], 2);

L.tileLayer(
  'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
  {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 20,
  }
).addTo(map);

fetch('http://localhost:8002')
  .then(response => response.json())
  .then(data => {
    // console.log(data.routeArray);
    const arr = data.routeArray;

    let prev;
    arr.forEach(ele => {
      const ip = ele[0];
      const latlon = ele[1];
      const city = ele[2];

      L.marker(latlon)
        .addTo(map)
        .bindPopup(
          L.popup({
            maxWidth: 100,
            minWidth: 25,
            autoClose: false,
            closeOnClick: false,
            className: 'host-popup',
          })
        )
        .setPopupContent(city)
        .openPopup();

      let randColor = generateNewColor();
      if (prev) {
        L.polyline([prev, latlon], {
          color: randColor,
        }).addTo(map);
      }

      prev = latlon;

      renderHost(city, ip, latlon, randColor);
    });
  });

///////////////////////////////////////////////////////
function renderHost(city, ip, latlon, color) {
  let html = `
    <li class="host" style="border-left: 5px solid ${color};">
      <h2 class="host__city">${city}</h2>
      <div class="host__details">
        <span class="host__icon">🖥️ </span>
        <span class="host__ip">${ip}<span>
      </div>
      <div class="host__details">
        <span class="host__icon">🌍 </span>
        <span class="host__coords">Coordinates:${latlon[0]},${latlon[1]}</span>
      </div>
    </li>`;

  form.insertAdjacentHTML('beforeend', html);
}

const hexCharacters = [
  0,
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
];

function generateNewColor() {
  let hexColorRep = '#';

  for (let index = 0; index < 6; index++) {
    const randomPosition = Math.floor(Math.random() * 16);
    hexColorRep += hexCharacters[randomPosition];
  }

  return hexColorRep;
}
