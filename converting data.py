Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1=input('please enter a whole number:')
please enter a whole number:1000
>>> num2=input("now enter another whole number:')
	   
SyntaxError: EOL while scanning string literal
>>> num2=input('now enter another whole number:')
now enter another whole number: 2000
>>> print('input is:',type(num1),type(num2))
input is: <class 'str'> <class 'str'>
>>> total=num1+num2
>>> print('Total:',total,type(total))
Total: 1000 2000 <class 'str'>
>>> total=int(num1)+int(num2)
>>> print('Total:',total,type(total))
Total: 3000 <class 'int'>
>>> 3+0
3
>>> total=float(num1)+float(num2)
>>> print('Total:'+str(total),type(total))
Total:3000.0 <class 'float'>
>>> 