distance = float(input())
input_measure = input()
output_measure = input()
result = 0

if input_measure == 'm':
    if output_measure == 'mm':
        result = distance * 1000
    elif output_measure == 'cm':
        result = distance * 100
    elif output_measure == 'm':
        result = distance
elif input_measure == 'cm':
    if output_measure == 'mm':
        result = distance * 10
    elif output_measure == "m":
        result = distance * 0.01
    elif output_measure == 'cm':
        result = distance
elif input_measure == 'mm':
    if output_measure == 'cm':
        result = distance * 0.1
    elif output_measure == 'm':
        result = distance * 0.001
    elif output_measure == 'mm':
        result = distance


print(f'{result:.3f}')