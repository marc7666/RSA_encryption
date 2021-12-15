"""
Author: Marc Cervera Rosell
"""

import time
from colorama import Fore
from sympy import randprime
from math import gcd


def generate_p_q():
    """
    Generates 2 prime random numbers
    :return: A tuple with the values p and q
    """
    p = 0
    q = 0
    while p == q:
        p = randprime(1, 20)
        q = randprime(1, 20)
    return p, q


def generate_n_fi(num_p, num_q):
    """
    Calculates the values of n and fi for a specific p and q
    :param num_p: integer
    :param num_q: integer
    :return: A tuple with the values n and fi
    """
    n = num_p * num_q
    fi = (num_p - 1) * (num_q - 1)
    return n, fi


def generate_e(fi):
    """
    Calculates the value of e
    :param fi: integer
    :return: The value of e such that gcd(e, fi) == 1 and e < fi
    """
    e = 2
    while gcd(e, fi) != 1 and e < fi:
        e += 1
    return e


def generate_d(fi, e):
    """
    Calculates the value of d
    :param fi: integer
    :param e: integer
    :return: The value of d such that d = (1 + k * fi) // e and (1 + k * fi) % e == 0
    """
    k = 0
    while (1 + k * fi) % e != 0:
        k += 1
    return (1 + k * fi) // e


def write_keys_in_files(n, e, d):
    """
    Writes the public and the private keys, as strings, in different files
    :param n: integer
    :param e: integer
    :param d: integer
    :return: None -> Void method
    """
    public_key = open('Public_key.txt', 'w')
    public_key.write(str(n) + "\n")
    public_key.write(str(e) + "\n")
    public_key.close()
    private_key = open('Private_key.txt', 'w')
    private_key.write(str(n) + '\n')
    private_key.write(str(d) + '\n')
    private_key.close()


def encrypt(message, e, n):
    """
    Computes the cryptogram for a message and public key specific
    :param message: integer
    :param e: integer
    :param n: integer
    :return: The cryptogram, computed by the formula
    """
    return (message ** e) % n


def decrypt(cryptogram, d, n):
    """
    Decrypts the message for a cryptogram and private key specific
    :param cryptogram: integer
    :param d: integer
    :param n: integer
    :return: The original message, computed by the formula
    """
    return (cryptogram ** d) % n


def write_p_q(p, q):
    """
    Writes the values p and q, as strings, in a file
    :param p: integer
    :param q: integer
    :return: None -> Void method
    """
    randoms = open('Values_of_p_and_q.txt', 'w')
    randoms.write(str(p) + "\n")
    randoms.write(str(q) + "\n")
    randoms.close()


def write_n_fi(n, fi):
    """
    Writes the values n and fi, as strings, in a file
    :param n: integer
    :param fi: integer
    :return: None -> Void method
    """
    n_fi_file = open('n_fi values.txt', 'w')
    n_fi_file.write(str(n) + "\n")
    n_fi_file.write(str(fi) + "\n")
    n_fi_file.close()


def write_e(e):
    """
    Writes the value e, as a string, in a file
    :param e: integer
    :return: None -> Void method
    """
    e_file = open('e_value.txt', 'w')
    e_file.write(str(e))
    e_file.close()


def write_d(d):
    """
    Writes the value d, as a string, in a file
    :param d: integer
    :return: None -> Void method
    """
    d_file = open('d_value.txt', 'w')
    d_file.write(str(d))
    d_file.close()


if __name__ == "__main__":
    """
    Main method. All the function calls are made here.
    """
    print(Fore.YELLOW, "Generating 2 prime random numbers...")
    p, q = generate_p_q()
    write_p_q(p, q)
    time.sleep(2)  # Waiting 2 seconds
    print(Fore.GREEN, "Take a look at ", repr(str("Values_of_p_and_q.txt")), "to know the values of the variables.")
    print(Fore.RED, "The first value is ", repr(str("p")), ", and the second one is ", repr(str("q")))

    num_n, num_fi = generate_n_fi(p, q)
    write_n_fi(num_n, num_fi)
    time.sleep(2)
    print(Fore.GREEN, "Take a look at", repr(str("n_fi values.txt")), "to know the values of the variables.")
    print(Fore.RED, "The first value is ", repr(str("n")), ", and the second one is ", repr(str("fi")))

    num_e = generate_e(num_fi)
    write_e(num_e)
    time.sleep(2)
    print(Fore.GREEN, "Take a look at", repr(str("e_value.txt")), "to know the value of the variable.")

    num_d = generate_d(num_fi, num_e)
    write_d(num_d)
    time.sleep(2)
    print(Fore.GREEN, "Take a look at", repr(str("d_value.txt")), "to know the value of the variable.")

    # Writing keys in correspondent files
    print(Fore.YELLOW, "Writing the keys in his correspondent file...")
    time.sleep(2)
    write_keys_in_files(num_n, num_e, num_d)
    pub_k = open('Public_key.txt', 'r')
    public_k = int(pub_k.readline()), int(pub_k.readline())
    pub_k.close()
    print("The public key is: ", public_k)
    pri_k = open('Private_key.txt', 'r')
    priv_k = int(pri_k.readline()), int(pri_k.readline())
    pri_k.close()
    print("The private key is: ", priv_k)

    # Encryption and decryption
    message_orig = 12
    num_crypto = encrypt(message_orig, num_e, num_n)
    print(Fore.MAGENTA, "Encrypting...")
    time.sleep(2)
    print("Cryptogram = ", num_crypto)

    orig_m = decrypt(num_crypto, num_d, num_n)
    print(Fore.MAGENTA, "Decrypting...")
    time.sleep(2)
    print("Original message = ", orig_m)
