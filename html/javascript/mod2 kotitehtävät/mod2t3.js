'use strict';

let dogNames = [];

for (let i = 0; i < 6; i++) {
    let name = prompt(`Enter the name of dog ${i +1}:`);
    dogNames.push(name);
}

dogNames.sort().reverse();

let dogListDiv = document.getElementById("dog-list");
let ul = document.createElement("ul");

dogNames.forEach(name => {
    let li = document.createElement("li");
    li.textContent = name;
    ul.appendChild(li);
})

dogListDiv.appendChild(ul);