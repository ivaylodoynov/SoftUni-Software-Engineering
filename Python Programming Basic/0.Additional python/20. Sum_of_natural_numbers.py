# Sum of natural numbers up to num
num = int(input('Enter a number: '))
if float(num) < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(int(float(num)) > 0):
       sum += float(num)
       num -= 1
   print("The sum is", sum)