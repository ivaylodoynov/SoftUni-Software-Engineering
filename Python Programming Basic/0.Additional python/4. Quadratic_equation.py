# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
a = 1
b = 5
c = 6
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))


# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module with user input figures
import cmath
a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')
# calculate the discriminant
d = (float(b)**2) - (4*float(a)*float(c))
# find two solutions
sol1 = (-float(b)-cmath.sqrt(d))/(2*float(a))
sol2 = (-float(b)+cmath.sqrt(d))/(2*float(a))
print('The solution are {0} and {1}'.format(sol1,sol2))