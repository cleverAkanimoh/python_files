import hashlib

from numpy import number

def saltPassword_sha512(password):
    salt = b'salt'
    hashed = hashlib.sha512(salt + password).hexdigest()
    print ("%s : %s" % (salt, hashed)) # Store these
    return hashed
plaintext_password = b'Password'
hashed_sha512 = saltPassword_sha512 (plaintext_password)

def text2int(msg):
    print (msg)

    try:
        # convert string to hex
        hexstr = msg.encode('hex')
        print (hexstr)

        # convert hex to integer
        integer_m = int(hexstr, 16)
        print (integer_m)

        # convert integer back to hex
        back2hex = format(integer_m, 'x')
        print (back2hex)

        # convert back to string
        evenpad = ('0' * (len(back2hex) % 2)) + back2hex
        plaintext = evenpad.decode('hex')
        print (plaintext)

    except:
        print('\nSomething went wrong. Invalid Format!!!\n')
    
text2int("Hello World")

import binascii
def text2int(msg):
    print (msg)

    # convert string to hex
    #hexstr = msg.encode('hex')
    msg = msg.encode()
    hexstr = binascii.hexlify(msg)
    print (hexstr)

    # convert hex to integer
    integer_m = int(hexstr, 16)
    print (integer_m)

    # convert integer back to hex
    back2hex = format(integer_m, 'x')
    print (back2hex)

    # convert back to string
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    #plaintext = evenpad.decode('hex')
    plaintext = binascii.unhexlify(evenpad)

    print (plaintext)

text2int("salt")
print('<info : Binascii hexlify Format" is working Fine>')

import binascii

def xorKey(secret):
    secret = secret.encode()
    hexstr = binascii.hexlify(secret)
    key = int(hexstr, 16)
    print ("key: ", key)
    return key

def xorEnc(msg, key):
    msg = msg.encode()
    hexstr = binascii.hexlify(msg)
    print ("hexstr: ", hexstr)
    ciphertext = int(hexstr, 16) ^ key
    print ("ciphertext: ", ciphertext)
    return ciphertext

def xorDec(msg, key):
    xorMsgKey = msg ^ key
    back2hex = format(xorMsgKey, 'x')
    print ("back2hex: ", back2hex)
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    plaintext = binascii.unhexlify(evenpad)
    print ("plaintext: ", plaintext)

    return plaintext

key = xorKey("...\nmysecret")
key2 = xorKey("wrongpass")
cipher = xorEnc('Hello world',key)
plain = xorDec(cipher,key)
wrongplain = xorDec(cipher, key2)

from binascii import hexlify, unhexlify

def otpSuperMsg(msg1, msg2):
    hex1 = hexlify(msg1)
    hex2 = hexlify(msg2)
    cipher1 = int(hex1, 16)
    cipher2 = int(hex2, 16)
    msg = cipher1 ^ cipher2
    return msg

def otpEnc(msg, key):
    superKey = int(msg, 16) ^ key
    return superKey

def otpDec(msg, key):
    xorMsgKey = msg ^ key
    back2hex = format(xorMsgKey, 'x')
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    plaintext = unhexlify(evenpad)
    return plaintext

realMessage = b"attackthematmidnight!"
decoyMessage= b"retreatanddonotattack"
msg = otpSuperMsg(realMessage, decoyMessage)

realMsg = hexlify(realMessage)
decoyMsg = hexlify(decoyMessage)
realKey = int(realMsg, 16) ^ msg
decoyKey = int(decoyMsg, 16) ^ msg
print ("\nThe secret message is: ", msg)
print ("The real key is: ", realKey)
print ("The decoy key is: ", decoyKey)
print ()
# choose either the decoy key or the real key
key = realKey
plain = otpDec(msg, key)
print (plain)
print ()
key = decoyKey
plain = otpDec(msg, key)
print ()
print (plain)

