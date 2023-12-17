# Python Program to find the area of triangle
a = 5
b = 6
c = 7
# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)




# Python Program to find the area of triangle to take inputs from the user
a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')

# calculate the semi-perimeter
s = (float(a) + float(b) + float(c)) / 2
# calculate the area
area = (s*(s-float(a))*(s-float(b))*(s-float(c))) ** 0.5
print('The area of the triangle is %0.2f' %area)
