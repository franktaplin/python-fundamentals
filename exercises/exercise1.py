# This is the part of the program for part 1 of the exercise.
# Can you make a typo that generates an error?
# for this part of the exercise I omitted the n in print. The line was prit('Hello World')
# I received this error: NameError: name 'prit' is not defined. Did you mean: 'print'?
# Can you make sense of the error message?
# Yes I can. The error is stating that the word prit is not a recognized Python command.
# IT then goes on to suggest that I might have misspelled the print command.
# Can you make a typo that doesn’t generate an error?
# Yes I changed Hello to Heloo. The line was print('Heloo World')
# The program compiled and printed Heloo World.
# Why do you think it didn’t make an error?
# There was no error reported because is the part of the line that is between the ' symbols is a string variable.
# A string variable is a series of characters. There is no spell checking or other modifications applied to the
# characters unless a command is issued to perform some sort of modification. It is very important to visually
# doublecheck your spelling when using strings.
print('Hello World')

# this part 2
# I ran import this from a python terminal prompt. It printed out "The Zen of Python" by Tim Peters
# the ouptut was:
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

print()

# This is part 3
message = 'May the Force be with you'
print(message)
# In the page 19 2-1 portion I create the variable message and assign the message 'May the Force be with you' to it.
# I then use the print command to print out the variable.
print()
# null line to separate parts of assignment
simple_message = 'Live Long and Prosper'
print(simple_message)
# In the page 19 2-2 portion I create the variable simple_message and assign the message 'Live Long and Prosper' to it.
# I then print it out using the print command
simple_message = 'Peace and Long life'
print(simple_message)
# In this portion I overwrite the message in the simple_message variable with the message 'Peace and Long Life'
# I then print out the value in the variable simple_message. This prints out the message 'Peace and Long Life' instead
# of 'Live Long and Prosper' because the original message has been overwritten by the second one.
print()


# This is part 4
def display_message():
    """displays a message."""
    print('This chapter of the book teaches about functions.')


display_message()
# This is page 131 part 8-1. I define a function named display_message that prints out the line of text:
# 'This chapter of the book teaches about functions.'
print()
# Null line to separate parts of program on screen.


def favorite_book(title):
    """Displays the title of one of my favorite books."""
    print(f'One of my favorite books is {title}.')


favorite_book("The Hobbit")
# This is page 131 part 8-2. I define a function named favorite_book that requires a parameter in order to function.
# In this case the parameter is the title of a book. When the function is run with a valid parameter it will
# print the line "One of my favorite books is " followed by the title of the book. The value that is put in between
# the () is the assigned to the title variable and the passed to the function. Printing the variable is done by
# inserting the f command into the print call. This tells the print command to insert the value that was
# assigned to the title variable when {title} is referenced in the print command.
