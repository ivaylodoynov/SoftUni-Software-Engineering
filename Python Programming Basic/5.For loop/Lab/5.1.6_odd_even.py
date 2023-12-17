text = str(input())

new_word = ''
for index, letter in enumerate(text):
    if index % 2 == 0:
        new_word += letter
print(new_word)