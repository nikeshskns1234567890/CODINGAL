const display = document.querySelector('.display')

const numberButtons = document.querySelectorAll('.number')

const operatorButtons = document.querySelectorAll('.operator')

let currentInput = ''

let previousInput = ''

let operator = null

function updateDisplay(value) {

    display.textContent = value || '0'

}

numberButtons.forEach(b => {

    b.addEventListener('click', () => {

        currentInput = currentInput + b.id

        updateDisplay(currentInput)

    })

})

operatorButtons.forEach(b => {

    b.addEventListener('click', () => {

        const id = b.id

        switch (id) {

            case 'clear':

                currentInput = ''

                previousInput = ''

                operator = null

                updateDisplay('')

                break

            case 'backspace':

                currentInput = currentInput.slice(0, -1)

                updateDisplay(currentInput)

                break;
            case 'equals':
                if (operator && previousInput && currentInput) {
                    result = claculate(parseFloat(previousInput), parseFloat
                        (currentInput), operator)
                }
                updateDisplay(result.toString())
                currentInput = result.toString()
                previousInput = ''
                operator = null
                break;
            case 'divide':
            case 'multiply':
            case 'subtract':
            case 'addition':

                if (previousInput && operator) {
                    result = calculate(parseFloat(previousInput), parseFloat
                        (currentInput), operator)
                } else {
                    previousInput = currentInput
                }
        }
        currentInput = '';
        operator = getOperatorSymbol(id);
        break;
            default:

        console.log('shdjf')

    }

    })

})

function getOperatorSymbol(id) {
    switch (id) {
        case 'divide':
            return '/';
        case 'multiply':
            return '*';
        case 'subtract':
            return '-';
        case 'addition':
            return '+';
        default:
            return '';
    }
}

function calculate(a, b, op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            return a / b;
        default:
            return b;
    }
}
