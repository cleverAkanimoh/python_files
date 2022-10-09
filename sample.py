Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import random, sample
>>> num=random()
>>> print('Random Float 0.0-1.0:',num)
Random Float 0.0-1.0: 0.15563397703912896
>>> num=int(num*10)
>>> print('Random Integer 0-9:',num)
Random Integer 0-9: 1
>>> nums=[];i=0
>>> while i<6:
	nums.append(int(random()*10)+1)
	i+=1

	
>>> print('Random Multiple Integers 1-10:',nums)
Random Multiple Integers 1-10: [1, 4, 9, 8, 2, 7]
>>> nums=sample(range(1,49),6)
>>> print('Random Integer Sample 1-49:',nums)
Random Integer Sample 1-49: [16, 13, 33, 44, 9, 42]
>>> 