name = input()

if name == 'banana' or name == 'apple' or name == 'kiwi' or name == 'lemon' or name == 'grapes' or name =='cherry':
    type = 'fruit'
elif name == 'tomato' or name == 'cucumber' or name == 'pepper' or name == 'carrot':
    type = 'vegetable'
else:
    type = 'unknown'

print(type)