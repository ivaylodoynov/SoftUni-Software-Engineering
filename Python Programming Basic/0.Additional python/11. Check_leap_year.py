# Python program to check if year is a leap year or not
year = input("Enter year: ")
# To get year (integer input) from the user
# year = int(input("Enter a year: "))
if (float(year) % 4) == 0:
   if (float(year) % 100) == 0:
       if (float(year) % 400) == 0:
           print("{0} is a leap year".format(float(year)))
       else:
           print("{0} is not a leap year".format(float(year)))
   else:
       print("{0} is a leap year".format(float(year)))
else:
   print("{0} is not a leap year".format(float(year)))