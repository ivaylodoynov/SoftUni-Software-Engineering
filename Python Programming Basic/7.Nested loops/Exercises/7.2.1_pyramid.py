n = int(input())

number = 1
cols = 1

while number <= n:
    for i in range(1, cols + 1):
        if number > n:
            break
        print(number, end=" ")
        number += 1
    # sliza na sledvashtiq red s tozi print
    print()
    cols += 1
