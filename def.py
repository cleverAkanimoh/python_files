Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> global_var=1
>>> def my_vars():
	print('Global variable:',global_var)

	
>>> def my_vars():
	print('Global variable:',global_var)
	local_var=2
	print('Local variable:',local_var)
	global inner_var
	inner_var=3

	
>>> my_vars()
Global variable: 1
Local variable: 2
>>> print('Coerced Global:',inner_var)
Coerced Global: 3
>>> 