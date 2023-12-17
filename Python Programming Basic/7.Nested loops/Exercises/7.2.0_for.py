#tova spira samo vtoroo uslovie
for i in range (1, 6):
    for j in range(1, 6):
        if j == 3:
            break
        print(f' {i}{j}')


# tova spira i purviq do 3kata
flag = False

for i in range (1, 6):
    if flag:
        break
    for j in range(1, 6):
        if j == 3:
            flag = True
            break
        print(f' {i}{j}')