age = float(input())
gender = input()
gender_char = gender.lower()[0]

if gender_char == 'm' and age >= 16:
        title = 'Mr.'
elif gender_char == 'm' and age < 16:
        title = 'Master'

elif gender_char == 'f' and age >= 16:
        title = 'Ms.'
elif gender_char == 'f' and age < 16:
        title = 'Miss'

print(title)