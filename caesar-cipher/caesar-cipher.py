message = input('Text: ')
key = int(input('Key: '))
mode = input('Mode e/d: ')
while not (mode == 'e' or mode == 'd'):
    print('Input e/d')
    mode = input('Mode e/d: ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        if mode == 'e':
            symbolindex = (SYMBOLS.find(symbol) + key) % len(SYMBOLS)
            translated += SYMBOLS[symbolindex]
        else:
            symbolindex = (SYMBOLS.find(symbol) - key + len(SYMBOLS)) % len(SYMBOLS)
            translated += SYMBOLS[symbolindex]
    else:
        translated += symbol 

if(mode == 'e'):
    print('Encripted: ', translated)
else:
    print('Decripted: ', translated)
