n1 = int(input())
n2 = int(input())

for number in range(n1, n2 + 1):
    evens_sum = 0
    odds_sum = 0
    counter = 1
    number_copy = number


    while number_copy> 0:
        last = number_copy % 10
        if counter % 2 == 0:
            evens_sum += last
        else:
            odds_sum += last
        number_copy = number_copy // 10
        counter += 1
    if evens_sum == odds_sum:
        print(number, end=" ")