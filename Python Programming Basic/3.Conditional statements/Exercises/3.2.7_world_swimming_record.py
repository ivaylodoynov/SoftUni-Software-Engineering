record = float(input())
meters = float(input())
time_per_meter = float(input())

time = meters * time_per_meter
water = int(meters / 15) * 12.5
total_time = time + water
second_needed = total_time - record

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {second_needed:.2f} seconds slower.')
