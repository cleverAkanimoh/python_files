Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> zoo=('Kangaroo','Leopard','Moose')
>>> print('Tuple:',zoo,'\tLength:',len(zoo))
Tuple: ('Kangaroo', 'Leopard', 'Moose') 	Length: 3
>>> print(type(zoo))
<class 'tuple'>
>>> bag={'Red','Green','Blue'}
>>> bag.add('yellow')
>>> print('\nSet:',bag,'\tLength:',len(bag))

Set: {'Green', 'yellow', 'Red', 'Blue'} 	Length: 4
>>> print(type(bag))
<class 'set'>
>>> print('\nIs Green In bag Set?:','Green' in bag)

Is Green In bag Set?: True
>>> print('\nIs Orange In bag Set?:','Orange' in bag)

Is Orange In bag Set?: False
>>> box={'Red','Purple','Yellow'}
>>> print('\nSet:',box,'\tLength:'len(box))
SyntaxError: invalid syntax
>>> print('\nSet:',box,'\tLength:',len(box))

Set: {'Yellow', 'Red', 'Purple'} 	Length: 3
>>> print('Common To Both Sets:',bag.intersection(box))
Common To Both Sets: {'Red'}
>>> 