imgName = str(input('\nEnter image name:\n>>> '))
print('...\n*** please wait ***\nThe program is looking for a file named: "%s" ' % (imgName))

fo = open(imgName, "rb")
image = fo.read()
fo.close()
print()
print("The secret key is 42.")
image = bytearray(image)
key = 42

for index, value in enumerate(image):
    image[index] = value^key

fo = open("e_%s" % (imgName), "wb")
fo.write(image)
fo.close()

print()
print('The image has been encrypted. Review "%s"' % (fo))

image = bytearray(image)
for index, value in enumerate(image):
    image[index] = key^value

fo = open("d_%s" % (imgName), "wb")
fo.write(image)
fo.close()
print()
print('The image has now been decrypted. Review "%s"' % (fo))