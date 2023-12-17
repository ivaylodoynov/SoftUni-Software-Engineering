age = int(input())
price_washing_mashine = float(input())
single_toy_price = int(input())

money_given = 10
savings = 0
toys_received_count = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        savings += money_given
        money_given += 10
        savings -= 1
    else:
        toys_received_count += 1

money_from_toys = toys_received_count * single_toy_price
savings += money_from_toys
money_left = abs(savings - price_washing_mashine)

if savings >= price_washing_mashine:
    print(f'Yes! {money_left:.2f}')

else:
    print(f'No! {money_left:.2f}')