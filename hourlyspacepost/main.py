from Crypto.Cipher import AES
from config.secureproperties import secure_properties
from nasa.nasaapi import APOD
import base64
import argparse


PARSER = argparse.ArgumentParser(description='HourlySpacePost Bot. Tweets space facts, news and images every hour.')
PARSER.add_argument('-e', '--env', type=str, required=False, help='Environment to run the bot (default: dev)', default='dev')
PARSER.add_argument('-k', '--key', type=str, required=False, help='Key required to decrypt/encrypt secure properties.')
ARGS = PARSER.parse_args()
SECURE_PROPERTIES = (secure_properties.get(ARGS.env)).copy()
# KEY = bytes(ARGS.key, 'utf-8')
KEY = b'megamanzero12345'
TWITTER_ID = 'client_id'
TWITTER_SECRET = 'client_secret'
NASA_KEY = 'nasa_key'


def main():
    for key, value in SECURE_PROPERTIES.items():
        cipher = base64.b64decode(value)
        decrypted_cipher = decrypt_property(cipher)
        SECURE_PROPERTIES.update({key: decrypted_cipher})

    for key, value in SECURE_PROPERTIES.items():
        print(f'{key}: {value}')

    nasa_apod = APOD(api_key='DEMO_KEY')
    print(nasa_apod.get())


def decrypt_property(cipher):
    iv = KEY
    decrypt_cipher = AES.new(KEY, AES.MODE_CBC, iv)
    cipher = decrypt_cipher.decrypt(cipher)

    return cipher.decode()


if __name__ == "__main__":
    main()
