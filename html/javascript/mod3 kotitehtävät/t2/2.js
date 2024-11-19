let targetElement = document.getElementById("target");

let firstItem = document.createElement("li");
firstItem.textContent = "First item";
targetElement.appendChild(firstItem);

let secondItem = document.createElement("li");
secondItem.textContent = "Second item";
secondItem.classList.add("my-item");
targetElement.appendChild(secondItem);

let thirdItem = document.createElement("li");
thirdItem.textContent = "Third item";
targetElement.appendChild(thirdItem);

targetElement.innerHTML = `
    <li>First item</li>
    <li class="my-item">Second item</li>
    <li>Third item</li>
    `;