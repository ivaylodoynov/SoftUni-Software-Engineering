number = int(input())

counter = 0
balance = 0.0

while counter < number:
    amount = float(input())
    if amount < 0:
        print(f'Invalid operation!')
        break
    else:
        balance += amount
        print(f'Increase: {amount:.2f}')
        counter += 1
print(f'Total: {balance:.2f}')
