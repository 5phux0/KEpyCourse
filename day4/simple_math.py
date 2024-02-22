"""
A collection of simple math operations
"""


def simple_add(a, b):
    """Calculates the sum of two numbers

    Parameters
    ----------
    a : number
        First number

    b : number
        Second number"""
    return a + b


def simple_sub(a, b):
    """Calculates the difference between two numbers

    Subtracts the subtrahend from the minuend

    Parameters
    ----------
    a : number
        Minuend

    b : number
        Subtrahend

    Returns
    ----------
    number
        Result of the subtraction operation"""
    return a - b


def simple_mult(a, b):
    """Calculates the product of two numbers

    Parameters
    ----------
    a : number
        Factor

    b : number
        Factor"""
    return a * b


def simple_div(a, b):
    """Calculates the quotient of two numbers

    Parameters
    ----------
    a : number
        Numerator

    b : number
        Denominator"""
    return a / b


def poly_first(x, a0, a1):
    """Calculates the value of a first degree polynomial

    Returns the result of the expression a0+a1*x

    Parameters
    ----------
    x : number
        Variable
    a0 : number
        Constant term
    a1 : number
        Coefficient"""
    return a0 + a1 * x


def poly_second(x, a0, a1, a2):
    """Calculates the value of a second degree polynomial

    Returns the result of the expression a0+a1*x+a2*x^2

    Parameters
    ----------
    x : number
        Variable
    a0 : number
        Constant term
    a1 : number
        First coefficient
    a2 : number
        Second coefficient"""
    return poly_first(x, a0, a1) + a2 * (x ** 2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
