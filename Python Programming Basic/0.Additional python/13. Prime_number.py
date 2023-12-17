# Program to check if a number is prime or not

num = int(input("Enter a number: "))

# To take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if float(num) > 1:
    # check for factors
    for i in range(2, int(float(num))):
        if (float(num) % i) == 0:
            print(float(num), "is not a prime number")
            print(i, "times", float(num) // i, "is", float(num))
            break
    else:
        print(float(num), "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(float(num), "is not a prime number")