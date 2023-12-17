screening_type = input()
rows = int(input())
columns = int(input())

income = 0
total_capacity = rows * columns
if screening_type == 'Premiere':
    income = total_capacity * 12
elif screening_type == 'Normal':
    income = total_capacity * 7.5
elif screening_type == 'Discount':
    income = total_capacity * 5

print(f'{income:.2f} leva')