# Caesar Cipher Hacker

message = input('Enter encrypted or decrypted text here: ')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

 # It is important to set translated to the blank string so that the previous iteration's value for translated is cleared.
    translated = ''

 # The rest of the program is the same as the original Caesar program:
 
 # runs the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

# handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
        else:
             # just add the symbol without encrypting/decrypting
            translated = translated + symbol

# displays the current key being tested, along with its decryption
    print('key #%s: %s' % (key, translated))

