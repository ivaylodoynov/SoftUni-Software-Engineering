# Python program to find the largest number among the three input numbers
# uncomment following lines to take three numbers from user

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

if (float(num1) >= float(num2)) and (float(num1) >= float(num3)):
   largest = float(num1)
elif (float(num2) >= float(num1)) and (float(num2) >= float(num3)):
   largest = float(num2)
else:
   largest = float(num3)
print("The largest number is", largest)