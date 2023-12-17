days = int(input())
type_of_room = input()
mark = input()

nights = days - 1

if type_of_room == 'room for one person':
    price = 18
    if nights < 10:
        discount = 0
    elif 10 <= nights <= 15:
        discount = 0
    elif nights > 15:
        discount = 0

elif type_of_room == 'apartment':
    price = 25
    if nights < 10:
        discount = 0.3
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.5

elif type_of_room == 'president apartment':
    price = 35
    if nights < 10:
        discount = 0.1
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.2

if mark =='positive':
    total_money = nights * price * (1-discount) * 1.25
else:
    total_money = nights * price * (1-discount) * 0.9

print(f'{total_money:.2f}')