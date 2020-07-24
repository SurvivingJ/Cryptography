from TranspositionCipher import encrypt_message, decrypt_message
import random

input_file = r'C:\Users\james\Desktop\Stuff\hkgisai ncnlk.txt'
output_file = 'Output_file.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    message = f.readlines()
f.close()
message = ''.join(message)

plain_text = decrypt_message(36, message)
print(plain_text)
'''
key = random.randint(5, 100)
encrypted_message = encrypt_message(key, message)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(encrypted_message)
    f.write('\n')
    f.write(str(key))
f.close()
'''