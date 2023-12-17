n = int(input())
leftsum = 0
rightsum = 0

for i in range(n):
    current_number = int(input())
    leftsum += current_number

for u in range(n):
    current_number = int(input())
    rightsum += current_number

if leftsum == rightsum:
    print(f'Yes, sum = {leftsum}')
else:
    diff = abs(rightsum - leftsum)
    print(f'No, diff = {diff}')
