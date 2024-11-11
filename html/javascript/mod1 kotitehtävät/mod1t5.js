let year = parseInt(prompt("Enter a year:"));
        console.log("Entered Year:", year); // Log the entered year

        // Determine if the year is a leap year
        let isLeapYear;

        if (year % 4 === 0) {
            console.log("The year is divisible by 4."); // Log divisibility by 4

            if (year % 100 === 0) {
                console.log("The year is also divisible by 100."); // Log divisibility by 100

                if (year % 400 === 0) {
                    console.log("The year is divisible by 400, so it is a leap year."); // Log divisibility by 400
                    isLeapYear = true;
                } else {
                    console.log("The year is not divisible by 400, so it is not a leap year."); // Log non-divisibility by 400
                    isLeapYear = false;
                }
            } else {
                console.log("The year is not divisible by 100, so it is a leap year."); // Log that it's not divisible by 100
                isLeapYear = true;
            }
        } else {
            console.log("The year is not divisible by 4, so it is not a leap year."); // Log non-divisibility by 4
            isLeapYear = false;
        }

        // Display the result on the HTML document
        document.getElementById("result1").innerHTML =
            `${year} is ${isLeapYear ? "a leap year" : "not a leap year"}.`;