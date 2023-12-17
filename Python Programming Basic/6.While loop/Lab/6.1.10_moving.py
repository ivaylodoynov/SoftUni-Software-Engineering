width = int(input())
lenght = int(input())
height = int(input())


space_volume = width * lenght * height
free_space = space_volume
is_done_moving = False
while free_space > 0:
    command = input()
    if command == 'Done':
        is_done_moving = True
        break

    box_count = int(command)
    free_space -= box_count

if is_done_moving:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')