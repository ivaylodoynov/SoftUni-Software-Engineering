number_of_tables = int(input())
lenght_of_rectangle_tables = float(input())
width_of_rectangle_tables =float(input())

area_pokrivka = number_of_tables * (lenght_of_rectangle_tables + 2*0.3) * (width_of_rectangle_tables + 2*0.3)
area_kareta = number_of_tables * (lenght_of_rectangle_tables/2) * (lenght_of_rectangle_tables/2)
price_in_USD = area_pokrivka * 7 + area_kareta * 9
price_in_BGN =price_in_USD * 1.85

print(f'{price_in_USD:.2f} USD')
print(f'{price_in_BGN:.2f} BGN')