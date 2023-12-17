days = float(input())
pastry_cookers = float(input())

cakes = float(input())
gofreta = float(input())
pancakes = float(input())

money_cakes = cakes * 45
money_gofreta = gofreta * 5.80
money_pancakes = pancakes *3.20

money = (money_cakes + money_gofreta + money_pancakes) * pastry_cookers
money_from_all_days = money * days
money_after_expenses = money_from_all_days - 1/8 * money_from_all_days
print(f'{money_after_expenses:.2f}')