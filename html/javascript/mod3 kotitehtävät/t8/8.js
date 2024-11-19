'use strict';

const num1Input = document.getElementById("num1");
const num2Input = document.getElementById("num2");
const operationSelect = document.getElementById("operation");
const resultParagraph = document.getElementById("result");

const calculateButton = document.getElementById("start");

calculateButton.addEventListener("click", function() {
    const num1 = parseFloat(num1Input.value);
    const num2 = parseFloat(num2Input.value);
    const operation = operationSelect.value;

    let result;

    if (isNaN(num1) || isNaN(num2)) {
        resultParagraph.textContent = "Please enter valid numbers.";
    }

    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'sub':
            result = num1 - num2;
            break;
        case 'multi':
            result = num1 * num2;
            break;
        case 'div':
            if (num2 === 0) {
                resultParagraph.textContent = "Error: Division by zero.";
                return;
            }
            result = num1 / num2;
            break;
        default:
            resultParagraph.textContent = "Please select a valid operation.";
            return;
    }
    resultParagraph.textContent = `Result: ${result}`;
})