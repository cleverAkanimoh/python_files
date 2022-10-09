Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> basket=['Apple','Bun','Cola']
>>> crate=['Egg','Fig','Grape']
>>> print('Basket list:',basket)
Basket list: ['Apple', 'Bun', 'Cola']
>>> print('Basket Element:',len(basket))
Basket Element: 3
>>> basket.append('Damson')
>>> print('Appended:',basket)
Appended: ['Apple', 'Bun', 'Cola', 'Damson']
>>> print('Last item Removed:',basket.pop())
Last item Removed: Damson
>>> print('Basket List:',basket)
Basket List: ['Apple', 'Bun', 'Cola']
>>> basket.extend(crate)
>>> print('Extended list:',basket)
Extended list: ['Apple', 'Bun', 'Cola', 'Egg', 'Fig', 'Grape']
>>> del basket[1]
>>> print('Item Removed:',basket)
Item Removed: ['Apple', 'Cola', 'Egg', 'Fig', 'Grape']
>>> del basket[1:3]
>>> print('Slice em)
      
SyntaxError: EOL while scanning string literal
>>> 
>>> print('Slice Removed:',basket)
Slice Removed: ['Apple', 'Fig', 'Grape']
>>> 