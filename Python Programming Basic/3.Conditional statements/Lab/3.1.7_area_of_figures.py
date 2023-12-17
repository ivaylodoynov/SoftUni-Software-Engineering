import math
type = input()
area = 0

if type == "square":
    side_a = float(input())
    area = side_a * side_a

elif type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif type == "triangle":
    side_a = float(input())
    vertical_height = float(input())
    area = side_a * vertical_height /2

elif type == "circle":
    from math import pi
    radius = float(input())
    area = pi * radius * radius

print(f'{area:.3f}')