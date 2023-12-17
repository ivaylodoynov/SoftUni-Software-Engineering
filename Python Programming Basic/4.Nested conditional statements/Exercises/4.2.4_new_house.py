type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

money_needed = 0

if type_of_flower == 'Roses':
    money_needed = number_of_flowers * 5
    if number_of_flowers > 80:
        money_needed = money_needed * 0.9

elif type_of_flower == 'Dahlias':
    money_needed = number_of_flowers * 3.8
    if number_of_flowers > 90:
        money_needed = money_needed * 0.85

elif type_of_flower == 'Tulips':
    money_needed = number_of_flowers * 2.8
    if number_of_flowers > 80:
        money_needed = money_needed * 0.85

elif type_of_flower == 'Narcissus':
    money_needed = number_of_flowers * 3
    if number_of_flowers < 120:
        money_needed = money_needed * 1.15

elif type_of_flower == 'Gladiolus':
    money_needed = number_of_flowers * 2.5
    if number_of_flowers < 80:
        money_needed = money_needed * 1.2


if money_needed <= budget:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {(budget - money_needed):.2f} leva left.')
else:
    print(f'Not enough money, you need {(money_needed - budget):.2f} leva more.')
