month = input()
days = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if days > 14:
        studio = 50 * 0.7
        apartment = 65 * 0.9

    elif days > 7:
        studio = 50 * 0.95
        apartment = 65

elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
    if days > 14:
        studio = 75.2 * 0.8
        apartment = 68.7 * 0.9


elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if days > 14:
        apartment = 77 * 0.9


print(f'Apartment: {days * apartment:.2f} lv.')
print(f'Studio: {days * studio:.2f} lv.')
