password = input('What is the password?: ')
if password == 'rosebud':
    print('Access granted.')
    
if password != 'rosebud':
        print('Access denied.')


password = input('What is the password?: ')
if password == 'rosebud':
    print('Access granted.')
else:
    print('Access denied, "Try again"')

numberOfEggs = int(input('enter egg value: '))
if numberOfEggs < 4:
    print('That is not that many eggs.')
elif numberOfEggs < 20:
    print('You have quite a few eggs.')
elif numberOfEggs > 20:
    print('You have a lot of eggs. Gross!')
else:
    print('Eat ALL the eggs!') 
