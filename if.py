if age < 18:
    print('просто нет')
else:
    print('ну ладно, уговорил')

if not is_user_banned:
    ban_user(user)

if team == 'mystic':
    print('Hi, blue team')
elif team == 'instinct':
    print('Hi, yellow team')
elif team == 'valor':
    print('Hi, red team')

    if team == 'mystic':
        if user_level >= 5:
            print('Welcome to the gym')
        else:
            print('Get more exp')