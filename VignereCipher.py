letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt_message(key, message):
    return translate_message(key, message, 'encrypt')

def decrypt_message(key, message):
    return translate_message(key, message, 'decrypt')

def translate_message(key, message, mode):
    translated = []

    key_index = 0
    key = key.upper()

    for ch in message:
        num = letters.find(ch.upper())
        if num != -1:
            if mode == 'encrypt':
                num += letters.find(key[key_index])
            elif mode == 'decrypt':
                num -= letters.find(key[key_index])
    
            num %= len(letters)

            if ch.isupper():
                translated.append(letters[num])
            elif ch.islower():
                translated.append(letters[num].lower())
            
            key_index += 1
            if key_index == len(key):
                key_index = 0
        
        else:
            translated.append(ch)
    return ''.join(translated)

key = 'LUCARIOFORTUITOUSMAGIC'
message = 'Ouxiu Pwqzyhoax Powx (Jata 19, 1862 – Xua 23, 1923) wra os Odxlqvoh hdikav hbq bvkors kay xksmapetb qq Agoiosycng Ovbjyjeizg. Dzlp ak Eoysiofqxh Ujeetin, Yyy Yfzy, yc r wcamwhygiypgo zcmztm, ms thhdxfnwp tu Kcebqlzkwxa lgxmk hbw suolcywg ow Uwhvrxf UvUcnzee, ejtfg a jbiisem ub Rofw Gnodgcmktp. Ps jbkxlmw hbw Veycke itdvz ws 1883, ggxhlbba lte tmze 17 sgaia gyiurcvz ohv fegkjthi ak Rsxizm cvlhclgtowpd njrfcumclm npx Bijfhkiueytn Lvwysu Lnimsm; zq wga qcxciemr f Qrmbweww hdikav th 1898. Duvt hmse uyktay s brungdmqr rb Ujcizybhkh Mzibmtdcvy, rvr boj tjxhwhlqd obu algszlssh zg 1905. Qpbzy az olnkny, je tcfyozeyl bbnwdcutnpakakm oyvcxnqvg ufp itavtnwtvl gyfzvn lbgwablovg, alqmgbwsu ixmqlhufoe lzqx mvuumbyg rgx xtfyffs, gvf scu rvucaoc bh 1908. Px eoaf tnm Lpmwik wfisi lydxfud kegzu wuvei ibi gvvlmmzs emrxqgo cp 1912, rvaiqhzga qg oh ggtiza qlqm\
yqg kcifyz Csmmut iwnwycglmg. Ms ctnmk zyxf tnm Elnjocqq Hvlkwp, tbx az 1922 wga qcxciemr fb Vicavcjsx pxqgdn. '
mode = 'decrypt' # Set to either 'encrypt' or 'decrypt'

if mode == 'encrypt':
    translated = encrypt_message(key, message)
elif mode == 'decrypt':
    translated = decrypt_message(key, message)

print(f'Key is {key}')
print(f'{mode}ed message:')
print(translated)