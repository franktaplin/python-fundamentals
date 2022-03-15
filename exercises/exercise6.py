# This is the section for part 1
print('This is Part 1')
print()
# This is the if statement
# if alien_color == 'green':
#   print('You scored 5 points!')

# This is the version where it is true
alien_color = 'green'
if alien_color == 'green':
    print('You scored 5 points!')

# This is the version where it is false
alien_color = 'red'
if alien_color == 'green':
    print('You scored 5 points!')

print()
# This is the section for part 2
print('This is Part 2')
print()

# This is the section that runs the if block
alien_color = 'green'
if alien_color == 'green':
    print('You gained 5 points!')
else:
    print('You gained 10 points!')

print()

# This is the section that runs the else block
alien_color = 'yellow'
if alien_color == 'green':
    print('You gained 5 points!')
else:
    print('You gained 10 points!')

print()

# This is the section for part 3
print('This is Part 3')
# This is section that runs if the alien is green
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')
print()

# This is section that runs if the alien is yellow
alien_color = 'yellow'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')
print()

# This is section that runs if the alien is red
alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')
print()

# This is the section for part 4
print('This is Part 4')
print()
person_age = 30
if person_age < 2:
    print('You are a baby.')
elif 2 <= person_age < 4:
    print('You are a toddler.')
elif 4 <= person_age < 13:
    print('You are a kid.')
elif 13 <= person_age < 20:
    print('You are a teenager.')
elif 20 <= person_age < 65:
    print('You are an adult.')
else:
    print('You are an elder.')

print()
# This is the section for part 5
print('This is part 5')
print()
# The argument that I used is named arg1. Boolean for 12 is True. Boolean for 1.2 is True. Boolean for 0 is False
# Boolean for 0.4 is True. Boolean for 0.0 is False.


def boolean_check(arg1):
    print(f'A boolean check for {arg1} returns {bool(arg1)}.')


boolean_check(12)


boolean_check(1.2)


boolean_check(0)


boolean_check(0.4)


boolean_check(0.0)
