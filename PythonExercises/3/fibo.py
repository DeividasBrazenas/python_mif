import math


def fibonacciNumberAtPosition(value):
    try:
        number = int(value)
    except ValueError:
        raise ValueError("Entered value is not a number")

    if math.floor(value) != value:
        raise ValueError("Value should be an integer")

    firstNumber, secondNumber = 0, 1
    count = 0

    if number <= 0:
        raise ValueError("Value should be greater than 0")
    elif number == 1:
        return 0
    else:
        while count < number - 1:
            nthNumber = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = nthNumber
            count += 1
        return firstNumber
