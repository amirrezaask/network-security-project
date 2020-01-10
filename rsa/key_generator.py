from math import gcd as bmm
from random import randrange


class KeyGenerator:
    @classmethod
    def are_non_relative(cls, x, y):
        return bmm(x, y) == 1

    @classmethod
    def __prime(cls, x):
        if x <= 1:
            return False

        if x <= 3:
            return True

        if x % 2 == 0 or x % 3 == 0:
            return False

        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i = i + 6

        return True

    @classmethod
    def __generate_2_prime_numbers(cls, s, e):
        rand = 0
        while not cls.__prime(rand):
            rand = randrange(s, e)
        p = rand
        rand = 0
        while not cls.__prime(rand):
            rand = randrange(s, e)
        q = rand

        return p, q

    @classmethod
    def __find_modular_inverse(cls, a, m):
        if bmm(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

        return u1 % m

    @classmethod
    def create_rsa_keys(cls, length=48):
        if length > 64:
            length = 63
        p, q = cls.__generate_2_prime_numbers(0, pow(2, length / 2))

        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = 0
        i = 2
        while i < phi_n:
            if cls.are_non_relative(i, phi_n):
                e = i
                break
            i += 1

        d = cls.__find_modular_inverse(e, phi_n)

        return n, e, d
