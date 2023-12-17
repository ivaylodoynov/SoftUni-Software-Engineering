animal = str(input())

if animal == 'dog':
    class_animal = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    class_animal = 'reptile'
else:
    class_animal = 'unknown'

print(class_animal)
