#Reversed cypher

message=input('\nPlease enter text to be encrypted:\n>>> ')
translated=''

i=len(message)-1
while i >=0:
    translated += message[i]
    i = i - 1
    
print('\nEncrypted text:\n>>> ',translated)
