from math import ceil
from random import randint

from miller_rabin_algo import miller_rabin, modular_exponentiation


def get_prime_number(length_bits, rabin_s=50):
    p = 2 ** length_bits
    for i in range(length_bits - 1):
        p += randint(0, 1) * (2 ** i)
    while miller_rabin(p, rabin_s):
        for i in range(length_bits - 1):
            p += randint(0, 1) * (2 ** i)
    return p


def rsa_keys():
    p = int(get_prime_number(1024))
    q = int(get_prime_number(1024))
    print('p', p)
    print('q', q)
    while abs(p - q) < 2 ** 30:
        p = int(get_prime_number(1024))
        q = int(get_prime_number(1024))
    n_key = p * q
    e = 2 ** 16 + 1
    while ((p - 1) * (q - 1)) % e != 0 and miller_rabin(p, 20):
        e += 2
    d = mod_linear_equation_solve(e,1,(p - 1) * (q - 1))
    return p, q, n_key, e, d[0]


def euclid_extended(a, b):
    if a == 0:
        x = 0
        y = 1
        return b, x, y

    d, x_1, y_1 = euclid_extended(b % a, a)
    x = y_1 - (b // a) * x_1
    y = x_1
    return d, x, y


# ax = b mod n
def mod_linear_equation_solve(a, b, n):
    d, x, y = euclid_extended(a, n)
    if b % d == 0:
        x_0 = (x * (b // d)) % n
        solutions = [(x_0 + i * (n // d)) % n for i in range(d)]
        return solutions



p_, q, n, e, d = rsa_keys()
print('public n', n)
print('public e', e)
print('secret d', d)

with open("open_key_n.txt", "w+", encoding="utf-8") as out:
    out.write(f"{n}")
with open("open_key_e.txt", "w+", encoding="utf-8") as out:
    out.write(f"{e}")
with open("secret_key_d.txt", "w+", encoding="utf-8") as out:
    out.write(f"{d}")