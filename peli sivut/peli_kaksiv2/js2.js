"use strict";
// Päävalikko
let gamer_tag = "";

/* Aloita peli */
document.getElementById("start-button").addEventListener("click", newGame);

/* Lataa peli modaali */
var modal = document.getElementById("myModal");
var btn = document.getElementById("load-button");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
  modal.style.display = "block";
};
span.onclick = function () {
  modal.style.display = "none";
};
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

/* Uusi peli */
async function newGame() {
  const name = document.getElementById("nimi").value.trim();
  const difficulty = document.getElementById("vaikeus").value;

  // Asetetaan pelaajan nimi ja vaikeustaso paikallisesti
  playerData.name = name;
  setDifficulty(difficulty);

  // Päivitetään käyttöliittymä
  updatePlayerInfo();
  /*document.getElementById("name-overlay").style.display = "none";*/

  // Hae pelidata palvelimelta
  try {
    const vastaus1 = await fetch(
      `http://127.0.0.1:3000/newgame/${name}/${difficulty}`
    );
    const vastaus1_json = await vastaus1.json();
    console.log(vastaus1_json);

    let gameArray = await fetch(`http://127.0.0.1:3000/gamelist`);
    let games = await gameArray.json();

    // Piilotetaan aloitusnäyttö ja ladataan peli
    const screen = document.getElementById("welcome-screen");
    screen.style.display = "none";
    loadGame(games.length - 1); // Lataa viimeisin peli
  } catch (error) {
    console.error("Virhe pelin aloituksessa:", error);
    alert("Pelin aloitus epäonnistui, tarkista palvelinyhteys.");
  }
}




/* Peli valikko */
async function loadList() {
  const gameArray = await fetch(`http://127.0.0.1:3000/gamelist`);
  const games = await gameArray.json();
  console.log(games);

  const target = document.getElementById("myModal");

  for (let i = 0; i < games.length; i++) {
    // Place
    let card = document.createElement("div");
    card.setAttribute("class", "modal-content");
    card.innerHTML = `
        <h2>${games[i].name}</h2>        
        <p>Vaikeus taso: ${games[i].difficulty} | Sijainti: ${games[i].location.country} | CO2: ${games[i].co2} | Rahat: ${games[i].money}€</p>
        <button onclick="loadGame('${[i]}')">Lataa Peli</button>
        `;
    target.appendChild(card);
  }
}

/* Pelin lataus */
async function loadGame(gamer_tag) {
  const screen = document.getElementById("welcome-screen");
  screen.style.display = "none";

  let gameArray = await fetch(`http://127.0.0.1:3000/gamelist`);
  let games = await gameArray.json();

  // Peli kartta
  const map = L.map("map1").setView([50.23, 13.74], 4);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  for (let i = 0; i < games[gamer_tag].airports.length; i++) {
    // Booleanit ja muut määritelmät
    let location = games[gamer_tag].location.name;
    let visited = games[gamer_tag].airports[i].visited;
    let goal = games[gamer_tag].airports[i].goal;

  // Kordinaatit ja lentokenttä
  let lentokentta = games[gamer_tag].airports[i].name;
  let lat = games[gamer_tag].airports[i].lat;
  let lon = games[gamer_tag].airports[i].lon;
  let coords = [lat, lon];

    let markerColor = "red"; // Oletusväri
    // Väri testi
    if (location == lentokentta) {
      markerColor = "blue";
    } else if (visited == true) {
      markerColor = "grey";
    }

    for (let j = 0; j < games[gamer_tag].flights.length; j++) {
      if (games[gamer_tag].flights[j].name == lentokentta) {
        markerColor = "green";
      }
      if (games[gamer_tag].flights[j].name == lentokentta && games[gamer_tag].flights[j].bonus_flight == true) {
        markerColor = "orange";
      }
    }

    if (goal == true){
      markerColor = "purple";
    }

    L.circleMarker(coords, {
      color: markerColor, // Väri
      radius: 6, // Pisteen koko
      weight: 2, // Reunan paksuus
      opacity: 1, // Täytteen läpinäkyvyys
      fillOpacity: 1, // Täytteen läpinäkyvyys
    }).addTo(map).bindPopup(`
          <b>${games[gamer_tag].airports[i].name}</b><br>
          <button onclick="showFlightDialog('${
            games[gamer_tag].airports[i].name
          }', ${JSON.stringify(coords)})">
            Valitse tämä lentokenttä
          </button>
        `);
  }
}


newGame();
loadList();

let playerData = {
  budget: 2000,
  emissions: 0,
  visitedAirports: 0,
  visitedCoordinates: [],
  currentAirport: null,
  currentAirportName: '',
  flightType: 'default',  // Tämä määrittelee oletusarvon
};

// Globaalit muuttujat ja pelaajan tiedot
const WEATHER_API_KEY = "95cb8ffa6452ef6b75e12f76180ac231"; // OpenWeatherMap API-avain


async function fetchGameData () {
  try {
    const response = await fetch("http://127.0.0.1:3000/game-data"); // Korvaa oikealla URL:illa
    if (!response.ok) {
      throw new Error("Virhe palvelimelta haettaessa pelidataa");
  }
    const gamedata = await response.json();
    updatePlayerDataFromServer(gamedata);
} catch (error) {
  console.error("Virhe pelidatan haussa", error);
  }
}

// *** Sivupalkin hallinta ***
function toggleSidebar(type) {
  document.getElementById(`sidebar-${type}`).classList.add("active");
}

function updatePlayerDataFromServer(gameData) {
  if (!gameData || typeof gameData !== "object") return;

  playerData.name = gameData.name || playerData.name;
  playerData.budget = gameData.money || playerData.budget;
  playerData.emissions = gameData.co2 || playerData.emissions;
  playerData.visitedAirports = gameData.visitedAirports || playerData.visitedAirports;
  if (gameData.location && gameData.location.lat && gameData.location.lon) {
    playerData.currentAirport = [gameData.location.lat, gameData.location.lon];
  }
  playerData.currentAirportName = gameData.location?.name || playerData.currentAirportName;
  updatePlayerInfo();
}

function setDifficulty(difficulty) {
  switch (difficulty) {
    case "helppo":
      playerData.budget = 2000;
      break;
    case "normaali":
      playerData.budget = 1500;
      break;
    case "vaikea":
      playerData.budget = 1000;
      break;
    default:
      playerData.budget = 500; // Oletus
  }
  console.log(`Vaikeustaso asetettu: ${difficulty}, budjetti: ${playerData.budget}`);
  updatePlayerInfo();
}

// Päivitä pelaajan tiedot käyttöliittymässä
function updatePlayerInfo() {
  document.getElementById("player-name").textContent = playerData.name || "N/A";
  document.getElementById("player-budjetti").textContent = `${playerData.budget.toFixed(2)} €`;
  document.getElementById("player-emissions").textContent = `${playerData.emissions.toFixed(2)} kg CO2`;
  document.getElementById("current-airport").textContent = playerData.currentAirportName || "Ei tietoja";
}

function closeSidebar(type) {
  document.getElementById(`sidebar-${type}`).classList.remove("active");
}

// *** Kokoruututila ***
function toggleFullScreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
}

// *** Pelin aloitus ***
function startGame() {
  const nameInput = document.getElementById("player-name").value.trim();
  if (!nameInput) {
    alert("Anna pelaajan nimi!");
    return;
  }
  playerData.name = nameInput;
  fetchGameData();
  document.getElementById("name-overlay").style.display = "none";
  /*playerData.currentAirport = [50.23, 13.74]; // Aloituskoordinaatit
  playerData.currentAirportName = "Praha"; // Asetetaan alkuperäinen kenttä nimeksi
  document.getElementById("player-name").textContent = playerData.name;
  document.getElementById(
    "player-budjetti"
  ).textContent = `${playerData.budget} €`;
  document.getElementById("name-overlay").style.display = "none";
  updatePlayerInfo();*/
  fetchWeather(playerData.currentAirport, updateWeatherInfo); // Hae säätiedot heti pelin alussa
}

// *** Säätiedon haku ***
function fetchWeather(coords, callback) {
  const [lat, lon] = coords;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${WEATHER_API_KEY}&units=metric&lang=fi`;

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Haku epäonnistui.");
      }
      return response.json();
    })
    .then((data) => {
      const weather = `
        Lämpötila: ${data.main.temp}°C<br>
        Tila: ${data.weather[0].description}<br>
        Tuuli: ${data.wind.speed} m/s
      `;
      callback(weather, data.name); // Lähetetään myös kaupungin nimi
    })
    .catch((error) => {
      console.error("Virhe säätietojen haussa:", error);
      callback("Säätiedot eivät ole saatavilla.");
    });
}

// *** Säätiedon näyttäminen ***
function updateWeatherInfo(weather, city) {
  document.getElementById("current-weather").innerHTML = `
    Nykyinen sää ${city}:<br>
    ${weather}
  `;
}

// *** Lentokentän valinta ***
function showFlightDialog(airportName, airportCoords) {
  fetchWeather(airportCoords, (weather, city) => {
    const dialog = document.createElement("div");
    dialog.className = "flight-dialog";
    dialog.innerHTML = `
      <h3>Lentokenttä: ${airportName}</h3>
      <p>${weather}</p>
      <p>Valitse lentoluokka:</p>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
      airportCoords
    )}, 'low')">Vähänpäästöinen</button>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
      airportCoords
    )}, 'medium')">Keskipäästöinen</button>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
      airportCoords
    )}, 'high')">Suurpäästöinen</button>
      <button onclick="closeDialog()">Peruuta</button>
    `;
    document.body.appendChild(dialog);
  });
}

// *** Sulje lentodialogi ***
function closeDialog() {
  const dialog = document.querySelector(".flight-dialog"); // Hakee ensimmäisen löytyvän flight-dialog-elementin
  if (dialog) {
    dialog.remove(); // Poistaa sen DOM:sta
  }
}

// Lentovalinnan vahvistus
function confirmFlight(airportName, airportCoords, flightType) {
  const costsPerKm = { low: 0.4, medium: 0.3, high: 0.2 };
  const emissionsPerKm = { low: 75, medium: 150, high: 300 };

  const distance = calculateDistance(playerData.currentAirport, airportCoords);
  const cost = distance * costsPerKm[flightType];
  const emission = distance * emissionsPerKm[flightType];

  if (playerData.budget < cost) {
    alert("Sinulla ei ole tarpeeksi rahaa tähän lentoon!");
    closeDialog();
    return;
  }

  // Päivitä pelaajan tiedot
  playerData.budget -= cost;
  playerData.emissions += emission / 1000; // Muutetaan kilogrammoiksi
  playerData.visitedAirports++;
  playerData.visitedCoordinates.push(airportCoords); // Lisää nykyinen sijainti käytyihin kenttiin
  playerData.currentAirport = airportCoords;
  playerData.currentAirportName = airportName; // Päivitetään lentokentän nimi

  updatePlayerInfo(); // Päivitetään pelaajan tiedot
  fetchWeather(playerData.currentAirport, updateWeatherInfo); // Päivitä säätiedot kenttämuutoksen jälkeen
  closeDialog(); // Sulje lentovalintadialogi
  checkGameStatus(); // Tarkista pelin tila
}


// *** Pelaajatietojen päivitys ***
function updatePlayerInfo() {
  // Päivitetään pelaajan tiedot
  document.getElementById(
    "player-budjetti"
  ).textContent = `${playerData.budget.toFixed(2)} €`;
  document.getElementById(
    "player-paastot"
  ).textContent = `${playerData.emissions.toFixed(2)} kg`;
  document.getElementById("player-kohde").textContent =
    playerData.visitedAirports;
  document.getElementById(
    "player-location"
  ).textContent = `Lentokenttä: ${playerData.currentAirportName}`; // Näytetään kenttä nimi
}

// *** Etäisyyden laskenta ***
function calculateDistance(coords1, coords2) {
  if (!coords1 || !coords2) return 0;
  const R = 6371; // Maapallon säde kilometreissä
  const dLat = toRad(coords2[0] - coords1[0]);
  const dLon = toRad(coords2[1] - coords1[1]);
  const lat1 = toRad(coords1[0]);
  const lat2 = toRad(coords2[0]);

  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

function toRad(value) {
  return (value * Math.PI) / 180;
}

// *** Pelin tilan tarkastus ***
function checkGameStatus() {
  if (playerData.visitedAirports >= 5) {
    alert("Onneksi olkoon! Olet voittanut pelin!");
    location.reload();
  } else if (playerData.budget <= 0) {
    alert("Rahasi loppuivat. Peli päättyi.");
    location.reload();
  }
}
