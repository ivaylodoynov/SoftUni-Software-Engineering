from math import floor

income = float(input())
grade = float(input())
min_income = float(input())

social_scholarship = 0
grade_scholarship = 0

if income < min_income:
    if grade > 4.5:
        social_scholarship = min_income * 0.35


if grade >= 5.5:
    grade_scholarship = grade * 25

if social_scholarship > grade_scholarship:
    print(f'You get a Social scholarship {floor(social_scholarship)} BGN')

elif grade_scholarship > social_scholarship:
    print(f'You get a scholarship for excellent results {floor(grade_scholarship)} BGN')
else:
    print('You cannot get a scholarship!')