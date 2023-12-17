budget = int(input())
season = str(input())
fishermans = int(input())

if season == 'Spring':
    boat = 3000
    if fishermans <= 6:
        boat = boat * 0.9
        if fishermans % 2 == 0:
            boat = boat * 0.85
    elif 7 <= fishermans <= 11:
        boat = boat * 0.85
        if fishermans % 2 == 0:
            boat = boat * 0.8
    elif fishermans >= 12:
        boat = boat * 0.75
        if fishermans % 2 == 0:
            boat = boat * 0.95

elif season == 'Summer':
    boat = 4200
    if fishermans <= 6:
        boat = boat * 0.9
        if fishermans % 2 == 0:
            boat = boat * 0.95
    elif 7 <= fishermans <= 11:
        boat = boat * 0.85
        if fishermans % 2 == 0:
            boat = boat * 0.95
    elif fishermans >= 12:
        boat = boat * 0.75
        if fishermans % 2 == 0:
            boat = boat * 0.95

elif season == 'Autumn':
    boat = 4200
    if fishermans <= 6:
        boat = boat * 0.9

    elif 7 <= fishermans <= 11:
        boat = boat * 0.85

    elif fishermans >= 12:
        boat = boat * 0.75

elif season == 'Winter':
    boat = 2600
    if fishermans <= 6:
        boat = boat * 0.9
        if fishermans % 2 == 0:
            boat = boat * 0.95
    elif 7 <= fishermans <= 11:
        boat = boat * 0.85
        if fishermans % 2 == 0:
            boat = boat * 0.95
    elif fishermans >= 12:
        boat = boat * 0.75
        if fishermans % 2 == 0:
            boat = boat * 0.95

if budget >= boat:
    money_left = budget - boat
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_not_enought = boat - budget
    print(f'Not enough money! You need {money_not_enought:.2f} leva.')
