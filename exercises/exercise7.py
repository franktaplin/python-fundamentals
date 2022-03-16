# This is the section for Part 1
# section 4-3 form book
print("This is Part 1")
print()


def basic_for():
    for number1 in range(1, 21):
        print(number1)


basic_for()
print()
# This is the section for Part 2
# section 4-6 from book
print("This is Part 2")
print()


def odd_numbers():
    for odd in range(1, 20, 2):
        print(odd)


odd_numbers()
print()
# This is the section for Part 3
# section 4-7 from book
print("This is Part 3")
print()


def by_threes():
    for triples in range(3, 31, 3):
        print(triples)


by_threes()
print()
# This is the section for Part 4
# section 4-8 from book
print("This is Part 4")
print()


def cubing():
    cubes = [value**3 for value in range(1, 11)]
    print(cubes)


cubing()
