'use strict';

const image = document.getElementById('target');
const trigger = document.getElementById('trigger');

trigger.addEventListener('mouseover', function() {
    image.src = 'img/picB.jpg';
});

trigger.addEventListener('mouseout', function() {
    image.src = 'img/picA.jpg';
});