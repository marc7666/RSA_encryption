"""
Authorship: Marc Cervera Rosell
"""


def xgcd(num1, num2):
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while num2 != 0:
        quotient = num1 // num2
        num1, num2 = num2, num1 - quotient * num2
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return num1, old_x, old_y
