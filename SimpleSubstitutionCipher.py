import sys
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def key_is_valid(key):
    key_list = list(key)
    letters_list = list(key)
    key_list.sort()
    letters_list.sort()

    return key_list == letters_list

def translate_message(key, message, mode):
    translated = ''
    charsA = letters
    charsB = key

    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
        charsA = ''.join(charsA)

    for ch in message:
        if ch.upper() in charsA:
            ch_index = charsA.find(ch.upper())
            if ch.isupper():
                translated += charsB[ch_index].upper()
            else:
                translated += charsB[ch_index].lower()
        else:
            translated += ch
    
    return translated

def encrypt_message(key, message):
    return translate_message(key, message, 'encrypt')

def decrypt_message(key, message):
    return translate_message(key, message, 'decrypt')

def get_random_key():
    key = list(letters)
    random.shuffle(key)
    return ''.join(key)

mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'
key = get_random_key()
message = 'David Hillhouse Buel (July 19, 1862 – May 23, 1923) was an American priest who became the president of Georgetown University. Born at Watervliet Arsenal, New York, to a distinguished family, he converted to Catholicism under the guidance of Michael McGivney, while a student at Yale University. He entered the Jesuit order in 1883, spending the next 17 years studying and teaching at Jesuit institutions throughout the Northeastern United States; he was ordained a Catholic priest in 1898. Buel then became a professor at Georgetown University, and was appointed its president in 1905. While in office, he curtailed intercollegiate athletics and instituted strict discipline, prompting resistance from students and parents, and his removal in 1908. He quit the Jesuit order several years later and secretly married in 1912, resulting in an outcry from his former Jesuit colleagues. He later left the Catholic Church, and in 1922 was ordained an Episcopal priest. '

if key_is_valid(key) is False:
    sys.exit('There is an error in the key or symbol set')
if mode == 'encrypt':
    translated = encrypt_message(key, message)
elif mode == 'decrypt':
    translated = decrypt_message(key, message)
print(f"Using key {key}")
print(f"The {mode}ed message is:")
print(translated)