from Cryptomath import gcd, findModInverse
import sys
import random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def get_key_parts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def check_keys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > (len(SYMBOLS) - 1):
        sys.exit(f'Key A must be greater than - and Key B must be between 0 and {len(SYMBOLS) - 1}')
    if gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit(f'Key A ({keyA}) and the symbol set size ({len(SYMBOLS)}) are not relatively prime.\
            Choose a different key.')

def encrypt_message(key, message):
    keyA, keyB = get_key_parts(key)
    check_keys(keyA, keyB, 'encrypt')
    cipher_text = ''

    for ch in message:
        if ch in SYMBOLS:
            ch_index = SYMBOLS.find(ch)
            cipher_text += SYMBOLS[(ch_index * keyA + keyB) % len(SYMBOLS)]
        else:
            cipher_text += ch
    return cipher_text

def decrypt_message(key, message):
    keyA, keyB = get_key_parts(key)
    check_keys(keyA, keyB, 'decrypt')
    plain_text = ''
    mod_inverse_of_keyA = findModInverse(keyA, len(SYMBOLS))

    for ch in message:
        if ch in SYMBOLS:
            ch_index = SYMBOLS.find(ch)
            plain_text += SYMBOLS[(ch_index - keyB) * mod_inverse_of_keyA % len(SYMBOLS)]
        else:
            plain_text += ch
    return plain_text

def get_random_key():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            return (keyA * len(SYMBOLS) + keyB)

#message =  """A computer would deserve to be called intelligent
#          if it could deceive a human into believing that it was human."""
message = """'A computer would deserve to be called intelligent if it could deceive a human
into believing that it was human.'' –Alan Turing"""
key = get_random_key()
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'

if mode == 'encrypt':
    translated = encrypt_message(key, message)
elif mode == 'decrypt':
    translated = decrypt_message(key, message)
print(f"Key is: {key}")
print(f"Mode is {mode}")
print(translated)

#print(get_random_key())