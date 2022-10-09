# Caesar Cipher
import pyperclip

message = input('Enter encrypted or decrypted text here: ')

# the encryption/decryption key
key = int(input('Enter key here: '))

# tells the program to encrypt or decrypt 
mode = str(input("Enter mode here: "))

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`a bcdefghijklmnopqrstuvwxyz{|}~ ' 

# stores the encrypted/decrypted form of the message
translated = ''

# Capitalize the string in message
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
# get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

# handles the wrap around if num is larger than the length of LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

# add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
# just  add the symbol without encrypting/decrypting
        translated = translated + symbol

#print the encrypted/decrypted string to the screen
print('This is the',mode,'ed'' text: '+ translated)

# copy the encrypted/decrypted string to the clipboard 
pyperclip.copy(translated)