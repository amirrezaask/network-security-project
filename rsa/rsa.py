from rsa.helpers import Helpers


class RSA:
    e, n, d = 0, 0, 0

    def __init__(self, n, e, d):
        if n is None or e is None or d is None:
            raise Exception('need all three arguments')
        self.n, self.e, self.d = n, e, d

    def encrypt(self, msg):
        """ encrypt encrypts input message"""
        numbers = Helpers.str_to_number(msg)
        pow_numbers = list()
        for n in numbers:
            pow_numbers.append(str(pow(n, self.e, self.n)))
        print(pow_numbers)
        return '-'.join(pow_numbers)

    def decrypt(self, cipher: str):
        """decrypt decrypts given cipher"""
        cipher = cipher.split("-")
        decrypted = list()
        for c in cipher:
            tmp = str(pow(int(c), self.d, self.n))
            if len(tmp) % 2 == 1:
                tmp = '0' + tmp
            decrypted.append(Helpers.number_to_str(tmp))
        return ''.join(decrypted)

