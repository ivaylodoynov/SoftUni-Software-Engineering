quantity_wine = float(input())
quantity_raki = float(input())
quantity_whisky = float(input())

price_raki = whisky * 0.5
price_wine = price_raki * 0.6
price_beer = price_raki * 0.2

sum_raki = quantity_raki * price_raki
sum_wine = quantity_wine * price_wine
sum_beer = quantity_beer * price_beer
sum_whiskey = quantity_whisky * whisky
sum_all = sum_beer + sum_wine + sum_raki + sum_whiskey
print(f'{sum_all:.2f}')