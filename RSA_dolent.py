def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extendGcd(a, b):  # El algoritmo euclidiano extendido aquí es un caso especial de gcd == 1
    if b == 0:
        x = 1
        y = 0
        return x, y
    else:
        x1, y1 = extendGcd(b, a % b)
        x = y1
        y = x1 - (int)(a / b) * y1
        return x, y


def fastMul(a, b, n):
    res = 1
    while b != 0:
        if b % 2 == 0:
            b = b / 2
            a = (a * a) % n
        elif b % 2 != 0:
            b = b - 1
            res = (res * a) % n
    return res


def generateKey(p, q):
    n = p * q
    fn = (p - 1) * (q - 1)
    e = 7  # eGenerally especifique 65537 directamente
    x, y = extendGcd(e, fn)
    if x < 0:  # Necesita una solución especial entre 1 y n, se puede demostrar que solo hay una
        x = x + fn
    d = x
    return (n, e), (n, d)


def encrypt(m, publicKey):
    n = publicKey[0]
    e = publicKey[1]
    c = fastMul(m, e, n)
    return c


def decrypt(c, privateKey):
    n = privateKey[0]
    d = privateKey[1]
    m = fastMul(c, d, n)
    return m


p = 3
q = 11
publicKey, privateKey = generateKey(p, q)
m = 25
print("Texto sin formato cifrado:% s" % m)
c = encrypt(m, publicKey)
print("Texto cifrado:% s" % c)
d = decrypt(c, privateKey)
print("Texto sin formato después del descifrado:% s" % d)
