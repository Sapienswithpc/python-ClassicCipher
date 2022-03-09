message = input('Text: ')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''


for key in range(1, len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolindex = (SYMBOLS.find(symbol) + len(SYMBOLS) - key) % len(SYMBOLS)
            translated += SYMBOLS[symbolindex]
        else:
            translated += symbol

    print('Key: %2s, Encrypted text: %s' % (key, translated))

print('Finished')

