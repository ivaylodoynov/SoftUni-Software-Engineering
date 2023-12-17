# Program to check Armstrong numbers in a certain interval
lower = int(input("Enter a lower number: "))
upper = int(input("Enter a upper number: "))
for num in range(int(float(lower)), int(float(upper)) + 1):
    # order of number
    order = len(str(num))

    # initialize sum
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)