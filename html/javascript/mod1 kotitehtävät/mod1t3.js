let num1 = parseInt(prompt("Enter the first integer:"));
let num2 = parseInt(prompt("Enter the second integer:"));
let num3 = parseInt(prompt("Enter the third integer:"));

let sum = num1 + num2 + num3;
let product = num1 * num2 * num3;
let average = sum / 3;

document.getElementById("output").innerHTML = `
            <strong>Sum:</strong> ${sum}<br>
            <strong>Product:</strong> ${product}<br>
            <strong>Average:</strong> ${average.toFixed(2)}`;