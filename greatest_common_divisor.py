"""
Authorship: Marc Cervera Rosell
"""


def gcd(num1, num2):
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
