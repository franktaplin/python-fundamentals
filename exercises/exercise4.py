# This is part 1 of the exercise
# This is section 2-8 from the book
print(5 + 3)
print(9 - 1)
print(2 * 4)
print(int(72 / 9))
print()

# This is section 2-9 from the book
favorite_number = int(19)
print(f'My favorite number is {favorite_number}.')
print()

# This is part 2 of the exercise
number1 = 456_234
number2 = 68_423_791
number3 = 13_794_628
number4 = 96_374


def number_sets(number_value):
    print(number_value)


number_sets(number1)
number_sets(number2)
number_sets(number3)
number_sets(number4)
print()
# This is part 3 of the exercise


def type_conversion(number_int, number_float):
    number_int = float(number_int)
    number_float = int(number_float)
    print(number_int, number_float)


type_conversion(34, 98.5)

# This is part 4 of the exercise


def movie_addiction():
    favorite_movie = input('What is your favorite movie? ')
    number_of_times = int(input('How many times have you seen it? '))
    print(f'I have seen {favorite_movie} {number_of_times} times.')


movie_addiction()
