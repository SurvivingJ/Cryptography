import re
import SimpleSubstitutionCipher
import wordPatterns
import copy
import makeWordPatterns

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
non_letters_or_space_pattern = re.compile('[^A-Z\s]')

def get_blank_cipher_letter_mapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
           'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
           'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
           'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def add_letters_to_mapping(letterMapping, cipherWord, candidate):
    for i in range(len(cipherWord)):
        if candidate[i] not in letterMapping[cipherWord[i]]:
            letterMapping[cipherWord[i]].append(candidate[i])

def intersect_mappings(mapA, mapB):
    intersected_mapping = get_blank_cipher_letter_mapping()
    
    for letter in letters:
        if mapA[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(mapA[letter])
        else:
            for mapped_letter in mapA[letter]:
                if mapped_letter in mapB[letter]:
                    intersected_mapping[letter].append(mapped_letter)
    
    return intersected_mapping

def remove_solved_letters_from_mapping(letterMapping):
    loop_again = True
    while loop_again:
        loop_again = False

        solved_letters = []
        for cipher_letter in letters:
            if len(letterMapping[cipher_letter]) == 1:
                solved_letters.append(letterMapping[cipher_letter][0])
        
        for cipher_letter in letters:
            for s in solved_letters:
                if len(letterMapping[cipher_letter]) != 1 and s in letterMapping[cipher_letter]:
                    letterMapping[cipher_letter].remove(s)
                    if len(letterMapping[cipher_letter]) == 1:
                        loop_again = True
    
    return letterMapping

def hack_simple_sub(message):
    intersected_map = get_blank_cipher_letter_mapping()
    cipherword_list = non_letters_or_space_pattern.sub('', message.upper()).split()

    for cipherword in cipherword_list:
        candidate_map = get_blank_cipher_letter_mapping()

        word_pattern = makeWordPatterns.getWordPattern(cipherword)
        if word_pattern not in wordPatterns.allPatterns:
            continue
            
        for candidate in wordPatterns.allPatterns[word_pattern]:
            add_letters_to_mapping(candidate_map, cipherword, candidate)
        
        intersected_map = intersect_mappings(intersected_map, candidate_map)
    
    return remove_solved_letters_from_mapping(intersected_map)

def decrypt_with_cipherletter_mapping(cipherText, letterMapping):
    key = ['x'] * len(letters)
    for cipher_letter in letters:
        if len(letterMapping[cipher_letter]) == 1:
            key_index = letters.find(letterMapping[cipher_letter][0])
            key[key_index] = cipher_letter
        else:
            cipherText = cipherText.replace(cipher_letter.lower(), '_')
            cipherText = cipherText.replace(cipher_letter.upper(), '_')
    
    return SimpleSubstitutionCipher.decrypt_message(key, cipherText)

message = '''Ouxiu Pwqzyhoax Powx (Jata 19, 1862 – Xua 23, 1923) wra os Odxlqvoh hdikav hbq bvkors kay xksmapetb qq Agoiosycng Ovbjyjeizg. Dzlp ak Eoysiofqxh Ujeetin, Yyy Yfzy, yc r wcamwhygiypgo zcmztm, ms thhdxfnwp tu Kcebqlzkwxa lgxmk hbw suolcywg ow Uwhvrxf UvUcnzee, ejtfg a jbiisem ub Rofw Gnodgcmktp. Ps jbkxlmw hbw Veycke itdvz ws 1883, ggxhlbba lte tmze 17 sgaia gyiurcvz ohv fegkjthi ak Rsxizm cvlhclgtowpd njrfcumclm npx Bijfhkiueytn Lvwysu Lnimsm; zq wga qcxciemr f Qrmbweww hdikav th 1898. Duvt hmse uyktay s brungdmqr rb Ujcizybhkh Mzibmtdcvy, rvr boj tjxhwhlqd obu algszlssh zg 1905. Qpbzy az olnkny, je tcfyozeyl bbnwdcutnpakakm oyvcxnqvg ufp itavtnwtvl gyfzvn lbgwablovg, alqmgbwsu ixmqlhufoe lzqx mvuumbyg rgx xtfyffs, gvf scu rvucaoc bh 1908. Px eoaf tnm Lpmwik wfisi lydxfud kegzu wuvei ibi gvvlmmzs emrxqgo cp 1912, rvaiqhzga qg oh ggtiza qlqm 
yqg kcifyz Csmmut iwnwycglmg. Ms ctnmk zyxf tnm Elnjocqq Hvlkwp, tbx az 1922 wga qcxciemr fb Vicavcjsx pxqgdn.'''
print('Hacking...')
letter_mapping = hack_simple_sub(message)
print('Mapping...')
print(letter_mapping)
print()
print('Original Ciphertext:')
print(message)
print()
hacked_message = decrypt_with_cipherletter_mapping(message, letter_mapping)
print(hacked_message)