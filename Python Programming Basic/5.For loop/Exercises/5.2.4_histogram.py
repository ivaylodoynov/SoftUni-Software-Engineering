n = int(input())

counter_200 = 0
counter_400 = 0
counter_600 = 0
counter_800 = 0
counter_801 = 0
percentage_200 = 0
percentage_400 = 0
percentage_600 = 0
percentage_800 = 0
percentage_801 = 0

for i in range(1, n + 1):
    element = int(input())
    if element < 200:
        counter_200 += 1
        percentage_200 = counter_200 / n * 100
    if 200 <= element < 400:
        counter_400 += 1
        percentage_400 = counter_400 / n * 100
    if 400 <= element < 600:
        counter_600 += 1
        percentage_600 = counter_600 / n * 100
    if 600 <= element < 800:
        counter_800 += 1
        percentage_800 = counter_800 / n * 100
    if element >= 800:
        counter_801 += 1
        percentage_801 = counter_801 / n * 100

print(f'{percentage_200:.2f}%')
print(f'{percentage_400:.2f}%')
print(f'{percentage_600:.2f}%')
print(f'{percentage_800:.2f}%')
print(f'{percentage_801:.2f}%')


