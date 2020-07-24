from TranspositionCipher import decrypt_message
from DetectEnglish import is_english

def hack_transposition(message):
    print("Stop by typing 'D' when prompted")
    print('Hacking...')

    for key in range(1, len(message)):
        print()
        print(f'Trying Key {key}')
        decrypted_text = decrypt_message(key, message)

        if is_english(decrypted_text) is True:

            print('Possible encryption hack:')
            print(f'Decrypted Text: {decrypted_text[:100]}')
            response = input('>')

            if response.strip().upper().startswith('D'):
                return decrypted_text
    
    return None

hacked_message = hack_transposition("""AaKoosoeDe5 b2 gmanw,forwneb  nglom,AigHt nie cetro d ro hAe snd iorr.u ieu v er Ne)alat r lw oCsaemie-sp ncieetgn iodhsriebruaisss retrm agAnlnoe(c -or nitiaicynhrh gaecnpeutaanrshicwsg etindeit n uhoedhsppmudg,tfl1e1 v1w shcnth  ekaBercaeu thlle  enlh na att  e mealefg eturmsa- e a0m82e8aEheideikfr ra'lhlrrceeyE.no euarisflhetcdba. t taa  toet NCsLc b17m5sn ma reno olbsya apor tn one dtes igmnoa yc r,iersfcegr""")

if hacked_message == None:
    print("Failed to hack encryption")
else:
    print(hacked_message)