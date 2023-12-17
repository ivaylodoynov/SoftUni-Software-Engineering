


# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]
divisible_by = int(input('Enter division number: '))
# use anonymous function to filter
result = list(filter(lambda x: (x % float(divisible_by) == 0), my_list))
# display the result
print("Numbers divisible by 13 are",result)