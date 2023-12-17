n = int(input())

counter = 0
min = 999999999
while counter < n:
    number = int(input())
    counter += 1
    if number < min:
        min = number
print(min)