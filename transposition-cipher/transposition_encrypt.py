def encrypt(message, key):
    key = int(key)
    translated = [''] * key

    for column in range(key):
        index = column
        
        while index < len(message):
            translated[column] += message[index]
            index += key
    return ''.join(translated)

def main():
    print('This is transposition encoder.')
    message = input('Text to encrypt: ')
    key = input('Key: ')

    translated = encrypt(message, key)
    print(translated + '|')

if __name__ == '__main__':
    main()


