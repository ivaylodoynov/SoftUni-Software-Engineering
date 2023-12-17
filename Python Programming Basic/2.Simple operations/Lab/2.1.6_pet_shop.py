dogs_number = int(input())
other_animals_number = int(input())

dogs_food_price = dogs_number * 2.5
other_animals_food_price = other_animals_number * 4
total_cost = dogs_food_price + other_animals_food_price
print(f' {total_cost:.2f} lv.')