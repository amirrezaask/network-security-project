import random
from collections import namedtuple


def get_primes(start, stop):
    if start >= stop:
        return []

    primes = [2]

    for n in range(3, stop + 1, 2):
        for p in primes:
            if n % p == 0:
                break
            else:
                primes.append(n)

    while primes and primes[0] < start:
        del primes[0]

    return primes


def are_relatively_prime(a, b):

    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def make_key_pair(length):

    if length < 4:
        raise ValueError('cannot generate a key of length less '
                         'than 4 (got {!r})'.format(length))

    n_min = 1 << (length - 1)
    n_max = (1 << length) - 1

    start = 1 << (length // 2 - 1)
    stop = 1 << (length // 2 + 1)
    primes = get_primes(start, stop)

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_candidates = [q for q in primes
                        if n_min <= p * q <= n_max]
        if q_candidates:
            q = random.choice(q_candidates)
            break
    else:
        raise AssertionError("cannot find 'p' and 'q' for a key of "
                             "length={!r}".format(length))


    stop = (p - 1) * (q - 1)
    for e in range(3, stop, 2):
        if are_relatively_prime(e, stop):
            break
    else:
        raise AssertionError("cannot find 'e' with p={!r} "
                             "and q={!r}".format(p, q))

    for d in range(3, stop, 2):
        if d * e % stop == 1:
            break
    else:
        raise AssertionError("cannot find 'd' with p={!r}, q={!r} "
                             "and e={!r}".format(p, q, e))

    return PublicKey(p * q, e), PrivateKey(p * q, d)


class PublicKey(namedtuple('PublicKey', 'n e')):

    __slots__ = ()

    def encrypt(self, x):

        return pow(x, self.e, self.n)


class PrivateKey(namedtuple('PrivateKey', 'n d')):

    __slots__ = ()

    def decrypt(self, x):

        return pow(x, self.d, self.n)

def str_to_number(s: str) -> int:
    number_hex = '0x'
    for c in s:
        hex_c = hex(ord(c))
        number_hex+=hex_c[2:]
    return int(number_hex, 16)   

    
def number_to_str(n: int) -> str: 
    hex_without_0x = str(hex(n))[2:]
    hexes = [hex_without_0x[i:i+2] for i in range(0, len(hex_without_0x), 2)]
    s = ''
    for hexe in hexes:
        hexe_ba_0x = '0x' + hexe
        hexe_vaghei = int(hexe_ba_0x, 16)
        c = chr(hexe_vaghei)
        s += c
    return s

if __name__ == '__main__':

    pub, prv = make_key_pair(6)
    enc = pub.encrypt(str_to_number("SALAM"))
    print(enc)
    dec = prv.decrypt(enc)
    print(dec)
    exit()