# Display the powers of 2 using anonymous function
num = int(input('Enter a number: '))
terms = int(input('Enter number of terms: '))

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))
# use anonymous function
result = list(map(lambda x: int(float(num)) ** x, range(int(float(terms)))))
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])