name = input()

grades_passed = 1
sum_grades = 0
grades_failed = 0
is_expelled = False
while grades_passed <= 12:
    grade = float(input())
    if grade >= 4.00:
        grades_passed += 1
        sum_grades += grade
    else:
        grades_failed += 1
        if grades_failed == 2:
            is_expelled = True
            print(f'{name} has been excluded at {grades_passed} grade ')
            break

#if grades_passed == 13:
if not is_expelled:

    avg_grade = sum_grades / 12
    print(f'{name} graduated. Average grade: {avg_grade:.2f}')

# Graduation Part 1

# name = input()

# grades = 1
# sum_grades = 0
# while grades <= 12:
#   grade = float(input())
#  if grade >= 4.00:
#     grades += 1
#    sum_grades += grade

# avg_grade = sum_grades / 12
# print(f'{name} graduated. Average grade: {avg_grade:.2f}')
