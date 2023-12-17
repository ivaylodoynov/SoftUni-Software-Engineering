city = str(input())
volume = float(input())

commision = -1
if city == 'Sofia':
    if 0 <= volume <= 500:
        commision = 0.05
    elif 500 < volume <= 1000:
        commision = 0.07
    elif 1000 < volume <= 10000:
        commision = 0.08
    elif volume > 10000:
        commision = 0.12

elif city == 'Varna':
    if 0 <= volume <= 500:
        commision = 0.045
    elif 500 < volume <= 1000:
        commision = 0.075
    elif 1000 < volume <= 10000:
        commision = 0.10
    elif volume > 10000:
        commision = 0.13

elif city == 'Plovdiv':
    if 0 <= volume <= 500:
        commision = 0.055
    elif 500 < volume <= 1000:
        commision = 0.08
    elif 1000 < volume <= 10000:
        commision = 0.12
    elif volume > 10000:
        commision = 0.145

if commision >= 0:
    print(f'{volume * commision:.2f}')
else:
    print('error')