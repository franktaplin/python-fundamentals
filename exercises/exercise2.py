# Frank Taplin INF 138 python fundamentals exercise 2
# Part 1 of the exercise is to write a function called simple(). Assign a different message to 5 variables
# and print each one.


def simple():
    """basic function that has 5 variables and prints out the message assigned to each one."""
    message_1, message_2 = 'We come in peace', 'Infinite Diversity in Infinite Combinations'
    message_3, message_4 = 'Today is a good day to die!', 'Resistance is Futile'
    message_5 = 'A Ferengi without profit is no Ferengi at all.'

    print(message_1), print(message_2), print(message_3), print(message_4), print(message_5)


simple()

# Part 2 of the exercise is to write a function called simple2().
# Assign a message to a variable, then print out that variable.
# Change the message and assign it to the variable again, but after the first print statement.
# Print the second message. Do these steps 2 more times. You should have 4 messages assigned to
# the same variable and 4 print functions showing the results.
print()


def simple2():
    """Function where you assign a message to a variable then print it. After that you change the message"""
    """ and print out the new message. Repeat process until there are a total of 4 messages."""
    first_message = 'There is no emotion. There is peace.'
    print(first_message)
    first_message = 'There is no ignorance. There is knowledge.'
    print(first_message)
    first_message = 'There is no passion. There is serenity.'
    print(first_message)
    first_message = 'There is no death. There is the Force.'
    print(first_message)


simple2()

# Part 3 of the exercise is to write a function called message that takes 1 argument.
# Inside that function, write a print function that takes the argument.
print()


def message(saying):
    """Function that takes an argument and then prints the argument"""
    print(saying)


message('Four score and seven years ago.')
