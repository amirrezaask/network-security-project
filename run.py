import click

from rsa import rsa

'''
Sample Usage:
    Generate:
        python3 run.py --mode g
    Encrypt:
        python3 run.py --mode e --e 7 --d 91635976162903 --n 160362984049267 --inpt SALAM

    Decrypt:
        python3 run.py --mode d --e 7 --d 91635976162903 --n 160362984049267 --cipher 124576655406223


'''

@click.command()
@click.option('--mode', '-m')
@click.option('--n')
@click.option('--e')
@click.option('--d')
@click.option('--inpt')
@click.option('--cipher')
def main(mode, n, e, d, inpt, cipher):
    if mode == 'g' or mode == 'generate' or mode == 'generate-keys':
        n, e, d = rsa.KeyGenerator.create_rsa_keys()
        print('n = {}, e={}, d={}'.format(n, e, d))

    elif mode == 'e' or mode == 'encrypt':
        print('n = {}, e={}, d={}'.format(n, e, d))
        r = rsa.RSA(int(n), int(e), int(d))
        print(r.encrypt(inpt))
    elif mode == 'd' or mode == 'decrypt':
        print('n = {}, e={}, d={}'.format(n, e, d))
        r = rsa.RSA(int(n), int(e), int(d))
        print(r.decrypt(int(cipher)))

if __name__ == '__main__':
    main()
