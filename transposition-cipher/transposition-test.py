import random, sys, transposition_encrypt, transposition_decrypt

def main():
    random.seed(42)
    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('No.%2s: %s...' % (i +1 ,message[:40]))

        for key in range (1, int(len(message) / 2)):
            encrypted = transposition_encrypt.encrypt(message, key)
            decrypted = transposition_decrypt.decrypt(encrypted, key)
            if decrypted != message:
                print('Mismatch! Key: %2s, Message: %s|' % (key, message))
                print('Decripted as: %s|' % decrypted)
                sys.exit()

    print('Test completed.')

if __name__ == '__main__':
    main()
