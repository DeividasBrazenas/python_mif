"""
>>> from fibo import fibonacciNumberAtPosition
>>> fibonacciNumberAtPosition(3)
1
>>> fibonacciNumberAtPosition(-3)
Traceback (most recent call last):
    ...
ValueError: Value should be greater than 0
>>> fibonacciNumberAtPosition(1)
1
>>> fibonacciNumberAtPosition(42)
165580141
>>> fibonacciNumberAtPosition("text")
Traceback (most recent call last):
    ...
ValueError: Entered value is not a number
>>> fibonacciNumberAtPosition(1.5)
Traceback (most recent call last):
    ...
ValueError: Value should be an integer

"""