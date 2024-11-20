'use strict';

document.getElementById("start").addEventListener("click", function() {
    const calculationInput = document.getElementById("calculation").value.trim();
    const resultParagraph = document.getElementById("result");

    let num1, num2, operator, result;

    if (calculationInput.includes("+")) {
        [num1, num2] = calculationInput.split("+").map(Number);
        operator = "+";
    } else if (calculationInput.includes("-")) {
        [num1, num2] = calculationInput.split("-").map(Number);
        operator = "-"
    } else if (calculationInput.includes("*")) {
        [num1, num2] = calculationInput.split("*").map(Number);
        operator = "*"
    } else if (calculationInput.includes("/")) {
        [num1, num2] = calculationInput.split("/").map(Number);
        operator = "/"
    } else {
        resultParagraph.textContent = "Invalid input. Please use +, -, * or /.";
        return;
    }

    if (isNaN(num1) || isNaN(num2)) {
        resultParagraph.textContent = "Invalid input. Please enter valid integers.";
    }

    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 === 0) {
                resultParagraph.textContent = "Error: Division by zero.";
                return;
            }
            result = Math.floor(num1 / num2);
            break;
        default:
            resultParagraph.textContent = "Please select a valid operation.";
            return;
    }
    resultParagraph.textContent = `Result: ${result}`;
});