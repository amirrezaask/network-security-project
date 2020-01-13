import time

import click

from rsa import rsa
from rsa import key_generator

'''
Sample Usage:
    Generate:
        python3 run.py --mode g
    Encrypt:
        python3 run.py --mode e --e 7 --d 91635976162903 --n 160362984049267 --inpt SALAM

    Decrypt:
        python3 run.py --mode d --e 7 --d 91635976162903 --n 160362984049267 --cipher 124576655406223

Program Flow:
    encrypt mode: user input -> helpers.str_to_number (for transforming given input to an integer number) -> rsa.encrypt -> return to user
    decrypt mode: user input -> rsa.decrypt -> helpers.number_to_str (transforming decrypted number to valid string ) -> return to user
    generate_keys: generate two random prime numbers named p and q -> generate n=>(p*q) and phi(n)=>(p-1)(q-1) -> generate e (which is the basis of our public key) -> generate d (basis of our private key)
'''


@click.command()
@click.option('--mode', '-m')
@click.option('--n')
@click.option('--e')
@click.option('--d')
@click.option('--length')
@click.option('--inpt')
@click.option('--cipher')
def main(mode, n, e, d, inpt, cipher, length):
    if mode == 'g' or mode == 'generate' or mode == 'generate-keys':
        start = time.time()
        n, e, d = key_generator.KeyGenerator.create_rsa_keys(int(length))
        end = time.time()
        print('n = {}, e={}, d={}'.format(n, e, d))
        print('Elapsed: {} seconds'.format(end - start))
    elif mode == 'e' or mode == 'encrypt':
        print('n = {}, e={}, d={}'.format(n, e, d))
        start = time.time()
        r = rsa.RSA(int(n), int(e), int(d))
        end = time.time()
        print(r.encrypt(inpt))
        print('Elapsed: {} seconds'.format(end - start))
    elif mode == 'd' or mode == 'decrypt':
        print('n = {}, e={}, d={}'.format(n, e, d))
        start = time.time()
        r = rsa.RSA(int(n), int(e), int(d))
        end = time.time()
        print(r.decrypt(cipher))
        print('Elapsed: {} seconds'.format(end - start))


if __name__ == '__main__':
    main()
