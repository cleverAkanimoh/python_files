# Transposition Cipher Encrypt/Decrypt File
import time, os, sys, transpositionEncrypt, transpositionDecrypt, random

def main():
    print('***        Welcome         ***\n====================================================')
    inputFilename = str(input('*** Enter Filename (e.g example.txt):\n>>> '))
    # BE CAREFUL! If a file with the outputFilename name already exists, this program will overwrite that file.
    if inputFilename is None:
        sys.exit('Ooops you forgot to enter file name. Run Again')

    if not inputFilename.endswith('.txt'):
        print('invalid extension, only ".txt" files allowed')
        sys.exit()

    myMode = str(input('\n*** Enter Cipher mode ("decrypt" or "encrypt". Cipher mode is not case sensitive):\n>>> ').lower()) # set to 'encrypt' or 'decrypt'
    if myMode is None:
        print('Ooops you forgot to enter mode. Run again')
        sys.exit()

    outputFilename = inputFilename[:-4] + '.' + myMode + 'ed.txt'

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file \'%s\'. Enter "c" to (C)ontinue or Enter any Key to (Q)uit?' % (outputFilename))
        response = input('>>> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # To print mode
    print('\n>>> Please wait %sing...\n' % (myMode.title()))

    # Measure how long the encryption/decryption takes.
    startTime = time.time()

    if myMode == 'encrypt':
        myKey = random.randint(4, round(len(content)/2))
        translated = transpositionEncrypt.encryptMessage(myKey, content)
        print('====================================================\n***        Important        ***\n... Your random key is "%s", Keep it safe.\n... If you forget key, run Encryption again.\n====================================================\n' % (myKey))
        if myKey is None:
            print('Ooops you forgot to enter key')
            sys.exit()

    elif myMode == 'decrypt':
        myKey = int(input('Decrypt key (Enter your "random key")\n>>> '))
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    else:
        print('Ooops! Seems you entered an invalid mode. Try "decrypt" or "encrypt". Cipher mode is not case sensitive')
        sys.exit()

    totalTime = round(time.time() - startTime, 2)

    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing "%s" (%s characters).\n====================================================' % (myMode, inputFilename, len(content)))

    print('%sion Endtime: %s seconds\n====================================================' % (myMode.title(), totalTime))

    print('%sed file is "%s"\n====================================================' % (myMode.title(), outputFilename))
    

# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
