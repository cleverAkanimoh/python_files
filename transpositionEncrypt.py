# Transposition Cipher Encryption
import pyperclip

def main():
    mymessage = input('Enter message here: ')
    mykey     = int(input('Enter key: '))

    ciphertext = encryptMessage(mykey, mymessage)

# Print the encrypted string in ciphertext to the screen, with a | (called "pipe" character) after it in case there are spaces at the end of the encrypted message.
    print(ciphertext + '|')

#copy the encrypted str in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # each string in ciphertext reps a column in the grid.
    ciphertext = [''] * key

    # loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        # keeps looping until pointer goes past the lenght of the message.
        while pointer < len(message):
            #place the character at the pointer in message at the end of the current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

# If transposition_cipher_encryption is run (instead of imported module) call the main() function.
if __name__ == '__main__':
    main()
