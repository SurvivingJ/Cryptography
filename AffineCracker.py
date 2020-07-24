import AffineCipher
import Cryptomath
from DetectEnglish import is_english

silent_mode = False
message = """'KM 5YnUlcFM15UptMtc3cFDcMl5MNcM eppctMaHlcppa9cHlMaLMalM 5UptMtc caDcMeMrUYeH
aHl5MNcpacDaH9MlrelMalM1e3MrUYeHb''M–KpeHMRUFaH9"""

def hack_affine(message):
    print("Hacking...")

    for key in range(len(AffineCipher.SYMBOLS)**2):
        keyA = AffineCipher.get_key_parts(key)[0]
        if Cryptomath.gcd(keyA, len(AffineCipher.SYMBOLS)**2) != 1:
            continue

        decrypted_text = AffineCipher.decrypt_message(key, message)

        if not silent_mode:
            print(f"Tried Key {key} ... {decrypted_text[:40]}")
        
        if is_english(decrypted_text):
            print()
            print("Possible encryption hack:")
            print(f"Key: {key}")
            print(F"Decrypted Message: {decrypted_text}")
            response = input('>')
        
            if response.strip().upper().startswith('D'):
                return decrypted_text
    return None

hacked_text = hack_affine(message)
print(hacked_text)