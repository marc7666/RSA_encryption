"""
@author: Marc Cervera Rosell
"""
import random
import extended_euclidean
import greatest_common_divisor
from colorama import Fore


def choose_e(fi):
    """
    Chooses a random number, 1 < e < fi, and checks if it is coprime with the fi, that is to say, gcd(e, fi) = 1
    """
    e = 0  # 0 can be divided between each of the numbers in the set of R.
    while greatest_common_divisor.gcd(e, fi) != 1:
        e = random.randint(2, fi)
    return e


def write_keys_in_file(n, e, d):
    public_k = open('Public key file', 'w')
    public_k.write(str(n) + '\n')
    public_k.write(str(e) + '\n')
    public_k.close()
    private_k = open('Private key file', 'w')
    private_k.write(str(n) + '\n')
    private_k.write(str(d) + '\n')
    private_k.close()


def generate_keys():
    """
       Selects two random prime numbers from a list of prime numbers which has
       values that go up to 100k. It creates a text file and stores the two
       numbers there where they can be used later. Using the prime numbers,
       it also computes and stores the public and private keys in two separate
       files.
    """
    p = random.randint(2, 10)
    q = random.randint(2, 10)
    n = p * q
    fi = (n - 1) * (q - 1)
    e = choose_e(fi)

    # Computing d. 1 < d < fi such that e * d = 1 mod fi. -> e and d are inverses in mod fi
    gcd, d, y = extended_euclidean.xgcd(e, fi)

    # In case 'd' is negative, it has to been transformed to positive
    if d < 0:
        d += fi

    write_keys_in_file(n, e, d)


def encrypt(message, public_k_file='Public key file', block_size=2):
    try:
        file = open(public_k_file)
    except FileNotFoundError:
        print(Fore.RED + "ERROR! File not found")
    else:
        n = int(file.readline())
        e = int(file.readline())
        file.close()

        encrypted = []
        cryptogram = -1

        if len(message) > 0:
            # Initialize cryptogram to the ASCII code of the first character of the message
            cryptogram = ord(message[0])

        for i in range(1, len(message)):
            # add cryptogram to the list if the mas block size is reached
            # Reset the cryptogram so we can continue adding ASCII codes
            if i % block_size == 0:
                encrypted.append(cryptogram)
                cryptogram = 0
            cryptogram = cryptogram * 1000 + ord(message[i])  # Multiplying by 1000 to shift the digits over to the
            # left by 3 places because ASCII codes are a max of 3 digits in decimal
        encrypted.append(cryptogram)  # The last block

        for i in range(len(encrypted)):  # Encrypting the numbers with the formula => number ** e mod n
            encrypted[i] = str((encrypted[i] ** e) % n)

        final_cryptogram = " ".join(encrypted)
        return final_cryptogram


def decrypt(blocks, block_size=2):
    fo = open('Private key file', 'r')
    n = int(fo.readline())
    d = int(fo.readline())
    fo.close()

    # turns the string into a list of ints
    list_blocks = blocks.split(' ')
    int_blocks = []

    for s in list_blocks:
        int_blocks.append(int(s))

    message = ""

    # converts each int in the list to block_size number of characters
    # by default, each int represents two characters
    for i in range(len(int_blocks)):
        # decrypt all of the numbers by taking it to the power of d
        # and modding it by n
        int_blocks[i] = (int_blocks[i] ** d) % n

        tmp = ""
        # take apart each block into its ASCII codes for each character
        # and store it in the message string
        for c in range(block_size):
            tmp = chr(int_blocks[i] % 1000) + tmp
            int_blocks[i] //= 1000
        message += tmp

    return message


if __name__ == "__main__":
    choose_again = input('Do you want to generate new public and private keys? (yes or no) ')
    if choose_again == 'yes':
        generate_keys()

    instruction = input('Would you like to encrypt or decrypt? (Enter encrypt or decrypt): ')
    if instruction == 'encrypt':
        message = input('What would you like to encrypt?\n')
        option = input('Do you want to encrypt using your own public key? (yes or no) ')

        if option == 'yes':
            print('Encrypting...')
            print(encrypt(message))
        else:
            file_option = input('Enter the file name that stores the public key: ')
            print('Encrypting...')
            print(encrypt(message, file_option))

    elif instruction == 'decrypt':
        message = input('What would you like to decrypt?\n')
        print('Decrypting...')
        print(message)
        m = encrypt(message)
        print(m)
        print(decrypt(m))
    else:
        print('That is not a proper instruction.')
