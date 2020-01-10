from math import gcd as bmm
from random import randrange

jadval = [
    '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '.', '?', ',', '-'
]


class RSA:
    e, n, d = 0, 0, 0

    def __init__(self, n, e, d):
        if n is None or e is None or d is None:
            raise Exception('need all three arguments')
        self.n, self.e, self.d = n, e, d

    def encrypt(self, msg):
        return pow(Helpers.text_to_int(msg), self.e, self.n)

    def decrypt(self, cipher):
        d = pow(cipher, self.d, self.n)
        print(d)
        return Helpers.int_to_text(d)


class KeyGenerator:
    @classmethod
    def are_non_relative(cls, x, y):
        return bmm(x, y) == 1

    @classmethod
    def is_prime(cls, x):
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
    def generate_2_prime_numbers(cls, s, e):
        rand = 0
        while not cls.is_prime(rand):
            rand = randrange(s, e)
        p = rand
        rand = 0
        while not cls.is_prime(rand):
            rand = randrange(s, e)
        q = rand

        return p, q

    @classmethod
    def find_modular_inverse(cls, a, m):
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
        p, q = cls.generate_2_prime_numbers(0, pow(2, length / 2))

        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = 0
        i = 2
        while i < phi_n:
            if cls.are_non_relative(i, phi_n):
                e = i
                break
            i += 1

        d = cls.find_modular_inverse(e, phi_n)

        return n, e, d


class Helpers:
    @classmethod
    def text_to_int(cls, s: str):
        s = s.upper()

        num_input = ""
        for char in s:
            if char in jadval:
                temp = jadval.index(char)
                if temp < 10:
                    num_input = num_input + "0" + str(temp)
                else:
                    num_input = num_input + str(temp)
            else:
                raise ValueError
        num_input = int(num_input)
        return num_input
    @classmethod
    def int_to_text(cls, num_input):
        if len(str(num_input)) % 2 == 1:
            decrypted = "0" + str(num_input)
        else:
            decrypted = str(num_input)
        str_input = [decrypted[i:i + 2] for i in range(0, len(decrypted), 2)]
        out = ""
        for kir in str_input:
            out = out + jadval[int(kir)]

        return out