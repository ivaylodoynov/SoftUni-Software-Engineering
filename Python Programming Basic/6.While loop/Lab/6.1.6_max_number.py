n = int(input())

count = 0
max = -9999999999
while count < n:
    num = int(input())
    count += 1
    if num > max:
        max = num
print(max)
