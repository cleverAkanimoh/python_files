Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nil=o
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    nil=o
NameError: name 'o' is not defined
>>> nil=0
>>> num=0
>>> top=1
>>> cap='A'
>>> low='a'
>>> print('equality:\t',nil,'==',num,nil==num)
equality:	 0 == 0 True
>>> print('equality:\t',cap,'==',low,cap==low)
equality:	 A == a False
>>> print('inequality:\t',nil,'!=',top,nil!=top)
inequality:	 0 != 1 True
>>> print('Greater:\t',nil,'>',top,nil>top)
Greater:	 0 > 1 False
>>> print(nil,'<',top,nil<top)
0 < 1 True
>>> 