# This is the section for Part 1
print('Part 1')
name = 'Frank'
print('Is name == Frank? I predict True.')
print(name == 'Frank')
print('Is name == to Seymour? I predict False.')
print(name == 'Seymour')
print()
age = 19
print('Is age == 19? I predict True.')
print(age > 18)
print('Is age == 21? I predict False.')
print(age >= 21)
print()
today = 'Saturday'
print('Is today == Saturday? I predict True.')
print(today == 'Saturday')
print('Is today == Sunday? I predict False.')
print(today == 'Sunday')
print()
pet_species = 'cat'
print('Is my pet cat a cat? I predict True.')
print(pet_species == 'cat')
print('Is my pet cat a dog? I predict False')
print(pet_species == 'dog')
print()
number = 45
print('Is number == 45? I predict True')
print(number == 45)
print('Is number == 58? I predict False.')
print(number == 58)
print()

# This is the section for Part 2
print('Part 2')
string = 'Now is the time for all good men'
print('Is string == Now is the time for all good men? I predict True.')
print(string == 'Now is the time for all good men')
print('Is string == to Friends, Romans, Countrymen? I predict False.')
print(string == 'Friends, Romans, Countrymen')
print()
full_name = 'Frank Taplin'
print('Is full_name.lower() == frank taplin? I predict True.')
print(full_name.lower() == 'frank taplin')
print('Is full_name.lower() == Frank Taplin? I predict False.')
print(full_name.lower() == 'Frank Taplin')
print()
age = 19
print('Can a 19 year old vote? I predict True.')
print(age > 18)
print('Can a 19 year old purchase alcohol? I predict False.')
print(age >= 21)
print()
number_test = 45
print('Is 45 between 40 and 50? I predict True')
print(number_test > 40 and number_test < 50)
print('Is 45 less than 40 or greater 47? I predict False.')
print(number_test < 40 or number_test > 47)
print()
feline_species = ['cat', 'lion', 'tiger']
print('Is my cat a feline? I predict True.')
print('cat' in feline_species)
print('Is my dog a feline? I predict False')
print('dog' in feline_species)
print()
even_numbers = [0, 2, 4, 6, 8, 10]
print('Is 3 not an even number between 0 and 10? I predict True.')
print(3 not in even_numbers)
print('Is 2 not an even number between 0 and 10? I predict False.')
print(2 not in even_numbers)
print()
# This is the section for Part 3
print('Part 3')


def math_operators(value1, value2):
    sum1 = value1 + value2
    diff = value1 - value2
    prod = value1 * value2
    quo = value1 / value2
    print(f'{value1} + {value2 } = {sum1}')
    print(f'{value1} - {value2} = {diff}')
    print(f'{value1} * {value2} = {prod}')
    print(f'{value1} / {value2} = {quo}')


math_operators(4, 2)


print()
# This is the section for Part 4
print('Part 4')


def assign_operators(value_assign):
    value_assign %= 10
    print(value_assign)
    value_assign -= 5
    print(value_assign)
    value_assign *= 3
    print(value_assign)
    value_assign += 8
    print(value_assign)


assign_operators(6)
