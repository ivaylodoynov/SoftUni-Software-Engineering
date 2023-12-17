lenght = int(input())
width = int(input())
height = int(input())
percent_taken = float(input())

voluma_of_the_acquirium = lenght * width * height
liters = voluma_of_the_acquirium * 0.001
taken_area = percent_taken * 0.01
volume_left = liters *(1-taken_area)
print(f'{volume_left:.3f}')