# RSA number encrypter and decrypter

In this file I am going to present a small explanation about each method inside the rsa.py file

## Keys generation:

### Method _generate_p_q()_

This method, returns 2 prime numbers between 1 and 20. These 2 numbers will not be equal.

### Method _generate_n_fi()_

This method, returns the values of the value of the keys 'n' and 'fi'. Both are goint to be used later.

### Method _generate_e()_

This method, searches a value of the key 'e', such that gcd(e, fi) == 1. The maximum value that can acquire 'e' is 'fi - 1' and the first value of 'e' is 2 because by definition;
1<e<fi.

### Method _generate_d()_

This method, calculates the value of the key 'd' by the formula: _(1 + k * fi) / e_, where 'k' goes from 0, and the condition to stop is to find a certain value of 'k' that makes the
previous formula returns an integer.

### Method _write_keys_in_files()_

This method, writes in different files the public and the private keys.

### Method _encrypt()_

This method, encrypts the message by the formula; _(message ** e) % n_. So, it uses the parameters of the public key to return a cryptogram.

### Method _decrypt()_

This method, takes the cryptogram and decrypts it by the formula; _(cryptogram ** d) % n_, thus returning the original message. To decrypt, the private key parameters are mandatory.

### Method _write_p_q()_:

This method, writes in a file the values of 'p' and 'q'.

### Method _write_n_fi()_:

This method, acts exactly like the previous one, but with the values of 'n' and 'fi'.

### Method _write_e()_

Another time, this method acts like the penultimate, but with the value of 'e'.

### Method _write_d()_:

This method acts like the antepenultimate.

### Method _main_

This is the main method where all the function calls are made.
