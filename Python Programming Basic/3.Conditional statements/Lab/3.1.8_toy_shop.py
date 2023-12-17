needed_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price_dolls = dolls_count * 3
total_price_puzzles = puzzles_count * 2.6
total_price_bears = bears_count * 4.1
total_price_minions = minions_count * 8.2
total_price_trucks = trucks_count * 2

total_price = total_price_dolls + total_price_puzzles + total_price_bears + total_price_minions + total_price_trucks
total_count = dolls_count + puzzles_count + bears_count + minions_count + trucks_count

if total_count >= 50:
    total_price *= 0.75

total_price *= 0.9

if total_price >= needed_price:
    print(f'Yes! {total_price-needed_price:.2f} lv left.')
else:
    print(f'Not enough money! {needed_price - total_price:.2f} lv needed.')