Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def echo(user, lang, sys):
	print('user:',user,'Language:',lang,'platform:',sys)

	
>>> echo('Mike','Python','Windows')
user: Mike Language: Python platform: Windows
>>> echo(lang='python',sys='dell win',user='clever')
user: clever Language: python platform: dell win
>>> def mirror(user='Clever',lang='Python'):
	print('\nUser:',user,'Language:',lang)

	
>>> mirror()

User: Clever Language: Python
>>> mirror(lang='Java')

User: Clever Language: Java
>>> mirror(user='AKANIMOH')

User: AKANIMOH Language: Python
>>> mirror('Eunice','c++')

User: Eunice Language: c++
>>> 