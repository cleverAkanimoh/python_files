dict={'name':'Clever','ref':'Python','sys':'win'}
print('Dictionary:',dict)
print('\nReference:',dict['ref'])
print('\nKeys:',dict.keys())
del dict['name']
dict['user']='Akanimoh'
print('\nDictionary:',dict)
print('\nDictionary:',dict)
print('\nIs there A name Key?:','name' in dict)
