# This is Part 1
print('This is Part 1')
print()
# This is exercise 5-8
print('This is exercise 5-8')
print()
user_list = ['FrankT19', 'Beaker510', 'admin', 'franktaplin', 'frankt']

for user_name in user_list:
    if user_name == 'admin':
        print('Hello admin, would you like to see a status report')
    else:
        print(f'Hello {user_name}, thank you for logging in.')
print()

# This is exercise 5-9
print('This is exercise 5-9')
print()
user_list = []

if user_list:
    for user_name in user_list:
        if user_name == 'admin':
            print('Hello admin, would you like to see a status report')
        else:
            print(f'Hello {user_name}, thank you for logging in.')
else:
    print('We need to find some users!')
print()

# This is Part 2
print('This is Part 2')
print()
current_users = ['jack', 'charlie', 'Mike', 'angela', 'jessie']
new_users = ['steph', 'mike', 'angela', 'john', 'frank']
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user} is not available. Please pick another username.')
    else:
        print(f'{new_user} is available.')
print()
# This is Part 3
print('This is Part 3')
print()
ordinal_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal in ordinal_list:
    if ordinal == 1:
        print(f'{ordinal}st')
    elif ordinal == 2:
        print(f'{ordinal}nd')
    elif ordinal == 3:
        print(f'{ordinal}rd')
    else:
        print(f'{ordinal}th')

print()
# This is Part 4
print('This is Part 4')
print()
exercise_dict = {'first_name': 'Frank', 'last_name': 'Taplin', 'age': 49, 'city': 'Belle Plaine'}
print(exercise_dict)
print()
# This is Part 5
print('This is Part 5')
print()
exercise_dict = {'first_name': 'Frank', 'last_name': 'Taplin', 'age': 49, 'city': 'Belle Plaine'}
exercise_dict2 = {'first_name': 'Rhonda', 'last_name': 'Williams', 'age': 47, 'city': 'Belle Plaine'}
exercise_dict3 = {'first_name': 'Mark', 'last_name': 'Ernst', 'age': 47, 'city': 'Reno'}
people = [exercise_dict, exercise_dict2, exercise_dict3]
for person in people:
    for info, answer in person.items():
        print(f'{info} : {answer}')
    print()
