from rsa.helpers import Helpers


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
        return Helpers.int_to_text(d)



