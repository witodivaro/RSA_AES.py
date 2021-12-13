from functools import reduce

from lib import mod
from Crypto.Util.number import getPrime


def gen_mod(size):
    p = getPrime(size - 1)
    q = getPrime(size + 1)

    N = p * q

    eulers_totient = (p - 1) * (q - 1)

    return (N, eulers_totient)


def gen_keys(eulers_totient):
    e = 3
    d = mod.inv_mod(e, eulers_totient)

    return (e, d)


def init(size):
    N, eulers_totient = gen_mod(size)
    e, d = gen_keys(eulers_totient)

    while (d == 0):
        N, eulers_totient = gen_mod(size)
        e, d = gen_keys(eulers_totient)

    return (N, e, d)


def encrypt(key, message, modulus):
    return mod.exp_mod(message, key, modulus)


def decrypt(key, encrypted, modulus):
    return mod.exp_mod(encrypted, key, modulus)
