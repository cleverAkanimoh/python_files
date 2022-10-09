Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> num=random.randint(1,20)
>>> flag=True
>>> guess=0
>>> print('Guess my number 1-20:',end='')
Guess my number 1-20:
>>> while flag==True:
	guess=input(15)
	if not guess.isdigit(15):
		print('Invalid! Enter only digits 1-20')
		break
	elif int(guess)<num:
		print('Too low, try again:',end='')
	elif int(guess)>num:
		print('Too high, try again:',end='')
	else:
		print('Correct... My number is'+guess)
		flag=False
