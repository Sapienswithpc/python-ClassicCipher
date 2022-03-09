import time, os, sys, transposition_encrypt, transposition_decrypt

def encrypt(message, key, outputfile):
    starttime = time.time()
    translated = transposition_encrypt.encrypt(message, key)
    outputobj = open(outputfile, 'w')
    outputobj.write(translated)
    outputobj.close()
    totaltime = round(time.time() - starttime, 2)
    print('Encription time: %s  Writed to \'%s\', %s words.' % (totaltime, outputfile, len(message)))

def decrypt(message, key, outputfile):
    starttime = time.time()
    translated = transposition_decrypt.decrypt(message, key)
    outputobj = open(outputfile, 'w')
    outputobj.write(translated)
    outputobj.close()
    totaltime = round(time.time() - starttime, 2)
    print('Decription time: %s  Writed to \'%s\', %s words.' % (totaltime, outputfile, len(message)))

def main():
    mode = 'a'
    while not (mode[0] == 'e' or mode[0] == 'd'):
        mode = input('Encrypt or decrypt? (e/d): ')
    mode = mode[0]
    inputfile = input('File to encrypt/decrypt: ')
    outputfile = input('File to output: ')

    while not os.path.exists(inputfile):
        print('File \'%s\' doesn\'t exist!' % inputfile)
        inputfile = input('File to encrypt/decrypt: ')
    
    if os.path.exists(outputfile):
        print('File exists! Do you want to overwrite \'%s\' ? ' % outputfile)
        response = input('(C)ontinue or (Q)uit: ')
        if not response.lower().startswith('c'):
            sys.exit()

    key = input('Key: ')

    fileobj = open(inputfile, 'r')
    message = fileobj.read()
    fileobj.close()

    if mode == 'e':
        print('Encripting...')
        encrypt(message, key, outputfile)
    else:
        print('Decripting...')
        decrypt(message, key, outputfile)

if __name__ == '__main__':
    main()

