
n = int(input())
numbers_sum = 0
max_num = -9999999999

for _ in range(n):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    numbers_sum += current_number

numbers_sum -= max_num

if numbers_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - numbers_sum)}')
