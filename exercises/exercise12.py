# This is Exercise 12
# This is Part 1
print('This is Part 1')
print()
print('Addition of two numbers.')
print()
try:
    alpha = input('Please type in the first number:')
    beta = input('Please type in the second number:')
    charlie = int(alpha) + int(beta)
    print(charlie)
except ValueError:
    print('You did not enter a number.')
print()

# This is Part 2
print('This is Part 2')
print()
print('Addition of two numbers.')
print('Type q instead of a number to quit.')
print()
run = True

while run:

    try:
        alpha = input('Please type in the first number:')
        if alpha == 'q':
            run = False
            continue
        beta = input('Please type in the second number:')
        if beta == 'q':
            run = False
            continue
        charlie = int(alpha) + int(beta)
        print(charlie)
    except ValueError:
        print('You did not enter a number.')
print()
# This is Part 3
print('This is Part 3')
print()
filename1 = 'cats.txt'
filename2 = 'dogs.txt'

try:
    with open(filename1, encoding='utf-8') as f:
        contents1 = f.read()
    print(contents1)
    print()

except FileNotFoundError:
    print(f'The file {filename1} cannot be found.')
    print()

try:
    with open(filename2, encoding='utf-8') as f:
        contents2 = f.read()
    print(contents2)
    print()

except FileNotFoundError:
    print(f'The file {filename2} cannot be found.')
    print()
print()
# This is Part 4
print('This is Part 4')
print()
filename1 = 'cats.txt'
filename2 = 'dogs.txt'

try:
    with open(filename1, encoding='utf-8') as f:
        contents1 = f.read()
    print(contents1)
    print()

except FileNotFoundError:
    pass

try:
    with open(filename2, encoding='utf-8') as f:
        contents2 = f.read()
    print(contents2)
    print()

except FileNotFoundError:
    pass
print()
