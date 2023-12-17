max_bad_grades = int(input())

bad_grades_counter = 0
total_grades = 0
sum_grades = 0
last_problem = ""
has_failed = True

while bad_grades_counter < max_bad_grades:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    grade = float(input())
    if grade <= 4:
        bad_grades_counter += 1
    sum_grades += grade
    total_grades += 1
    last_problem = problem_name

if bad_grades_counter == max_bad_grades:
        print(f'You need a break, {bad_grades_counter} poor grades.')

else:
    print(f'Average score: {(sum_grades/total_grades):.2f}')
    print(f'Number of problems: {total_grades}')
    print(f'Last problem: {last_problem}')