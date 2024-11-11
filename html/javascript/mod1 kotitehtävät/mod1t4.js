let studentName = prompt("Enter your name:");
console.log("Student's Name:", studentName);

let houseNumber = Math.floor(Math.random() * 4) + 1;
console.log("Generated House Number:", houseNumber);

let house;
if (houseNumber === 1) {
    house = "Gryffindor";
} else if (houseNumber === 2) {
    house = "Slytherin";
} else if (houseNumber === 3) {
    house = "Hufflepuff";
} else {
    house = "Ravenclaw";
}
console.log("Assigned House:", house); // Log the assigned house to the console

document.getElementById("result").innerHTML = `${studentName}, you are ${house}!`;