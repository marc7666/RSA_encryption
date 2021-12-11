"""
@author: Marc Cervera Rosell
"""
import math
import random


def is_prime(number):
    """
    This method checks if the parameter is prime
    :return: True if the parameter is prime and False otherwise
    """
    for i in range(2, number):
        if number % i == 0:
            return False
        return True


def generate_randoms():
    """
    This method generates two random numbers that are going to be used later
    :return: Two integers p and q
    """
    p = 4
    q = 4
    while is_prime(p) == False or is_prime(q) == False:
        p = random.randint(2, 10)
        q = random.randint(2, 10)
    return p, q


def calc_e(fi):
    e = 2
    while math.gcd(e, fi) != 1:
        e += 1
    return e


def calc_d(fi, e):
    k = 0
    d = (1 + k * fi) / e
    while (1 + k * fi) % e != 0:
        k += 1
        d = (1 + k * fi) / e
    return int(d)


def generate_keys():
    p, q = generate_randoms()
    n = p * q
    fi = (p - 1) * (q - 1)
    e = calc_e(fi)
    d = calc_d(fi, e)
    return (n, e), (n, d), (p, q, fi)


def encrypt(public_k, message):
    res = 1
    i = 0
    while i < public_k[1]:
        res = res * message
        i += 1
    res = res % public_k[0]
    return res


def decrypt(cryptogram, private_k):
    res = 1
    t = 0
    while t < private_k[1]:
        res = res * cryptogram
        t += 1
    res = res % private_k[0]
    return res


if __name__ == "__main__":
    public_key, private_key, randoms = generate_keys()
    print("Public key = ", public_key, " private key = ", private_key, " Randoms = ", randoms)
    print("p =", randoms[0], " q = ", randoms[1], " fi = ", randoms[2], " n = ", public_key[0], " e = ", public_key[1],
          " d = ", private_key[1])
    m = 2
    print("Message = ", m)
    c = encrypt(public_key, m)
    print("Cryptogram = ", c)
    orig_m = decrypt(c, private_key)
    print("Original message = ", orig_m)
    print("joder")