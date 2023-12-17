budget = float(input())
statists = int(input())
price_for_statist = float(input())

decor = budget * 0.1
if statists > 150:
    total_price_statists = price_for_statist * statists * 0.9
else:
    total_price_statists = price_for_statist * statists

total = decor + total_price_statists

if total > budget:
    not_enough_money = total - budget
    print('Not enough money!')
    print(f'Wingard needs {not_enough_money:.2f} leva more.')

else:
    money_left = budget - total
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')