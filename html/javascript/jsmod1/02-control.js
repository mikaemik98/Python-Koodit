'use strict';

// arvotaan testinumero (0-1)
const randomNumber = Math.random();
// else-haaran testaamista varten kovakoodattu arvo
// const randomNumber = 0.503
console.log('arvottu numero', randomNumber);

// ehtolause, ehdon täytyy olla aina true/false
// 49.9% todennäköisyys kruuna/klaava
if (randomNumber < 0.495) {
    console.log('kruuna');
} else if (randomNumber > 0.505) {
    console.log('klaava');
} else {
    console.log('kolikko jää kantilleen');
}

console.log('suoritus jaktuu ehtolauseen jälkeen');
/*
const cabinClass = prompt('Enter the cabin class (A/B/C).');
switch (cabinClass) {
    case 'A':
        console.log('Top deck cabin with window.');
        break;
    case 'B':
        console.log('Top deck cabin without window.');
        break;
    case 'C':
        console.log('Windowless cabin under the car deck.');
        break;
    default:
        console.log('Invalid cabin class.');
}
*/

// toistorakenteet eli silmukat eli loopit
// kuinka monta heittoa menee, että kolikko jää kyljelleen?
let throwCount = 0;
let stillThrowing = true;
while (stillThrowing) {
    const randomNumber = Math.random();
    throwCount++;
    if (randomNumber < 0.495) {
        console.log('kruuna');
    } else if (randomNumber > 0.505) {
        console.log('klaava');
    } else {
        console.log('kolikko jää kantilleen');
        console.log('Heittojen lk', throwCount);
        stillThrowing = false;
    }
}

// simppeli for-silmukka
for (let i = 1; i <= 100; i*=2) {
    console.log("iin arvo", i);
}

// kuinka monta heittoa menee keskimäärin, että kolikko jää kantilleen
const throwCounts = [];
for (let i=0; i<1000; i++) {
    let throwCount = 0;
    let stillThrowing = true;
    while (stillThrowing) {
        const randomNumber = Math.random();
        throwCount++;
        if (randomNumber < 0.495) {
            console.log('kruuna');
        } else if (randomNumber > 0.505) {
            console.log('klaava');
        } else {
            console.log('kolikko jää kantilleen');
            console.log('Heittojen lk', throwCount);
            throwCounts.push(throwCount);
            stillThrowing = false;
        }
    }
}
console.log("Heittojen lukumäärät: ", throwCounts);

// lasketaan heittomäärien summa for-silmukalla
let sum=0;
for (let i=0; i<throwCounts.length; i++) {
    sum += throwCounts[i];
}
console.log("Heittojen ka:", sum/throwCounts.length);