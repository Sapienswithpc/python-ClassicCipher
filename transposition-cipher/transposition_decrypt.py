import math

def decrypt(message, key):
    key = int(key)
    column = math.ceil(len(message) / key)
    translated = [''] * column
    empty = (column * key) - len(message) #empty box
    messageindex = 0 #index in message

    for row in range(key):
        index = 0
        while index < column:
            if not(((index + 1) == column) and ((row + empty) >= key)):
                translated[index] += message[messageindex]
                messageindex += 1
            index += 1
    return ''.join(translated)

def main():
    print('This is transposition decoder.')
    message = input('Text to Decrypt: ')
    key = input('Key: ')
    print(decrypt(message, key) + '|')

if __name__ == '__main__':
    main()
