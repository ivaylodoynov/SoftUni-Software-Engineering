import math
L = float(input())
W = float(input())
A = float(input())
area_of_the_rectangular_room_in_centimeters = (L * 100) * (W * 100)
size_of_the_squared_wardrobe = pow(A *100, 2)

size_of_the_bench = area_of_the_rectangular_room_in_centimeters / 10

free_space = area_of_the_rectangular_room_in_centimeters - size_of_the_squared_wardrobe - size_of_the_bench
number_of_people_possible = free_space / (40 + 7000)

print(math.floor(number_of_people_possible))