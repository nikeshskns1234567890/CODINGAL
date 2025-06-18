const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter first number: ", (num1) => {
    rl.question("Enter second number: ", (num2) => {
        num1 = Number(num1);
        num2 = Number(num2);

        console.log("Addition: " + (num1 + num2));
        console.log("Subtraction: " + (num1 - num2));
        console.log("Multiplication: " + (num1 * num2));
        console.log("Division: " + (num1 / num2));
        console.log("Modulo: " + (num1 % num2));

        rl.close();
    });
});
