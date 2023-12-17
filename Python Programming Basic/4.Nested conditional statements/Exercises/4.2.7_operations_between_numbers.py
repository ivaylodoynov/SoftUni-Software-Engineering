n1 = int(input())
n2 = int(input())
operation = input()

if operation == '+':
    result = n1 + n2
    operator = '+'
    if result % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd_even}')

elif operation == '-':
    result = n1 - n2
    operator = '-'
    if result % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd_even}')

elif operation == '*':
    operator = '*'
    result = n1 * n2
    if result % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {odd_even}')

elif operation == '/':
    operator = '/'
    if n2 == 0:
        print (f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} {operator} {n2} = {result:.2f}')

elif operation == '%':
    operator = '%'
    if n2 == 0:
        print (f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} {operator} {n2} = {result}')