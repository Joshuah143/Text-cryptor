import base64
import hashlib
import sys
from cryptography.fernet import Fernet, InvalidToken


def encrypt(password: str = None, to_encrypt: str = None, computer=False):
    if password is None:
        password = input('PASSWORD: ')
    if to_encrypt is None:
        to_encrypt = input('TO ENCRYPT: ')
    result = Fernet(base64.urlsafe_b64encode(hashlib.sha3_512(password.encode())
                                             .digest()[:32])).encrypt(bytes(to_encrypt.encode())).decode()
    return [result, f'Token: {result}']


def decrypt(password: str = None, to_decrypt: str = None, computer=False):
    if password is None:
        password = input('PASSWORD: ')
    if to_decrypt is None:
        to_decrypt = input('TO DECRYPT: ')
    while True:
        try:
            token = Fernet(base64.urlsafe_b64encode(hashlib.sha3_512(password.encode())
                                                    .digest()[:32])).decrypt(bytes(to_decrypt.encode())).decode()
            return [token, f'Message: {token}']
        except InvalidToken:
            if not computer:
                print('INVALID TOKEN\nTry checking the password and the token')
            elif computer:
                return ['NO VALID TOKEN', 'INVALID TOKEN\nTry checking the password and the token']
            continue


if __name__ == '__main__':
    print('Thank you for using my command line tool for message encryption. '
          'Please remeber that ALL STRINGS ARE CASE SENSITIVE.\n'
          'If you have an issue email me at joshua.himmens@icloud.com')
    args = sys.argv
    if 'decode' in args:
        print(decrypt(args[args.index('decode') + 1], args[args.index('decode') + 2]))
    elif 'encode' in args:
        print(encrypt(args[args.index('encode') + 1], args[args.index('encode') + 2]))
    else:
        choice = input('DECODE OR ENCODE (encode/decode): ').upper()
        if choice == 'DECODE':
            print(decrypt()[1])
        elif choice == 'ENCODE':
            print(encrypt()[1])


class ShortVersion:
    @staticmethod
    def encode(password: str, to_encrypt: str):
        return Fernet(base64.urlsafe_b64encode(hashlib.sha3_512(password.encode())
                                               .digest()[:32])).encrypt(bytes(to_encrypt.encode())).decode()

    @staticmethod
    def decode(password: str, to_decrypt: str):
        Fernet(base64.urlsafe_b64encode(hashlib.sha3_512(password.encode())
                                        .digest()[:32])).decrypt(bytes(to_decrypt.encode())).decode()
