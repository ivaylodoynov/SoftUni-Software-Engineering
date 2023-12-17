numbers_count = int(input())

sum_numbers = 0
for counter in range(numbers_count):
    current_number = int(input())

    sum_numbers += current_number
    #print(f'current_sum_numbers: {sum_numbers}')

print(sum_numbers)