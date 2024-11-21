'use strict';
console.log('script start');

async function fetchImages() {
    const response = await fetch('pics.json');
    if (response.ok) {
        const pics = await response.json();
        console.log('kuvat:', pics)
        for (const pic of pics) {
            const imgElem = document.createElement('img');
            imgElem.src = pic.address;
            imgElem.alt = pic.description;
            document.querySelector('#images').append(imgElem);
        }
    }
}
fetchImages();
//fetch('pics.json');

//chuck norris api esim ja virheen käsittely
async function getAJoke() {
    const outputElem = document.querySelector('#joke');
    try {
        const response = await fetch('https://api.chucknorris.io/jokes/random');
        console.log('joke response', response);
        if (!response.ok) {
            // status koodi jotain muuta kuin ok (ei 2xx)
            throw new Error(response.status.toString());
        }
        const joke = await response.json();
        console.log('vitsi: ', joke.value);
        outputElem.textContent = joke.value;
    } catch (error) {
        console.error(error);
        outputElem.textContent = "Vitsin haku epäonnistui."
    }
}

document.querySelector('#get-joke')
    .addEventListener('click', getAJoke);
//getAJoke();

// Esimerkki oman flask serverin käytöstä

async function fetchAirport(icao) {
    // TODO: lisää virheen käsittely
    const response = await fetch('http://127.0.0.1:5000/airport/' + icao);
    const airport = await response.json();
    //console.log('airport data', airport);
    // TODO: add data to dom (näytä käyttäjälle)
    return airport;
}
//fetchAirport('efhk');
const form = document.querySelector('#airport-form');
form.addEventListener('submit', async function(event) {
    event.preventDefault();
    // haetaan viittaus input-elementtii ja sen arvo (käyttäjän syöte)
    const userInput = form.querySelector('input').value;
    const airport = await fetchAirport(userInput);
    console.log(airport);
});

document.querySelector('#joke').textContent = "odotetaan vieläkin";

console.log('script end');