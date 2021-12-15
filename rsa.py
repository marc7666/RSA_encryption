import time
from colorama import Fore
from sympy import randprime
from math import gcd


def generate_p_q():
    p = 0
    q = 0
    while p == q:
        p = randprime(1, 20)
        q = randprime(1, 20)
    return p, q


def generate_n_fi(num_p, num_q):
    n = num_p * num_q
    fi = (num_p - 1) * (num_q - 1)
    return n, fi


def generate_e(fi):
    e = 2
    while gcd(e, fi) != 1 and e < fi:
        e += 1
    return e


def generate_d(fi, e):
    k = 0
    while (1 + k * fi) % e != 0:
        k += 1
    return (1 + k * fi) // e


def write_keys_in_files(n, e, d):
    public_key = open('Public_key.txt', 'w')
    public_key.write(str(n) + "\n")
    public_key.write(str(e) + "\n")
    public_key.close()
    private_key = open('Private_key.txt', 'w')
    private_key.write(str(n) + '\n')
    private_key.write(str(d) + '\n')
    private_key.close()


def encrypt(message, e, n):
    return (message ** e) % n


def decrypt(cryptogram, d, n):
    return (cryptogram ** d) % n


def write_p_q(p, q):
    randoms = open('Values_of_p_and_q.txt', 'w')
    randoms.write(str(p) + "\n")
    randoms.write(str(q) + "\n")
    randoms.close()


if __name__ == "__main__":
    print(Fore.YELLOW, "Generating 2 prime random numbers...")
    # p, q = generate_p_q()
    p = 5
    q = 11
    write_p_q(p, q)
    time.sleep(2)  # Waiting 2 seconds
    print(Fore.GREEN, "Take a look at ", repr(str("Values_of_p_and_q.txt")), "to know the values of the variables.")
    print(Fore.RED, "The first value is ", repr(str("p")), ", and the second one is ", repr(str("q")))
    # num_n, num_fi = generate_n_fi(p, q)
    num_n = 55
    num_fi = 40
    print("n = ", num_n, " fi = ", num_fi)
    # num_e = generate_e(num_fi)
    num_e = 3
    print("e = ", num_e)
    # num_d = generate_d(num_fi, num_e)
    num_d = 27
    print("d = ", num_d)
    write_keys_in_files(num_n, num_e, num_d)
    pub_k = open('Public_key.txt', 'r')
    public_k = int(pub_k.readline()), int(pub_k.readline())
    pub_k.close()
    print("Public key: ", public_k)
    pri_k = open('Private_key.txt', 'r')
    priv_k = int(pri_k.readline()), int(pri_k.readline())
    pri_k.close()
    print("Private key: ", priv_k)
    message_orig = 12
    num_crypto = encrypt(message_orig, num_e, num_n)
    print("Cryptogram = ", num_crypto)
    orig_m = decrypt(num_crypto, num_d, num_n)
    print("Original message = ", orig_m)
