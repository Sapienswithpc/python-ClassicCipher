message = input('Enter text: ')
encoded = ''

for i in range(len(message)):
	encoded += message[len(message) - i - 1]

print('Encoded texts: ', encoded)
