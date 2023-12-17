# Python program to display all the prime numbers within an interval
lower = int(input("Enter a lower number: "))
upper = int(input("Enter a upper number: "))
print("Prime numbers between", float(lower), "and", float(upper), "are:")
for num in range(int(float(lower)), int(float(upper)) + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

