n = int(input())
oddsum = 0
evensum = 0

for i in range(1, n+1):
    element = int(input())
    if i % 2 == 0:
        evensum += element
    else:
        oddsum += element

if evensum == oddsum:
    print('Yes')
    print(f'Sum = {evensum}')
else:
    diff = abs(evensum - oddsum)
    print('No')
    print(f'Diff = {diff}')
