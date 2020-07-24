message = ""
translated = ""

#SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(SYMBOLS)):
    translated = ""
    for ch in message:
        if ch in SYMBOLS:
            symbolIndex = SYMBOLS.find(ch)
            translatedIndex = symbolIndex - i

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + ch
    print(f"Key #{str(i)}: {translated}")
    print("")