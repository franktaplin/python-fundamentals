# This is exercise 13
# This is part 1
print('This is Part 1')
print()
# This is exercise 8-15
print('This is exercise 8-15')
print()
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
print()

# This is exercise 8-16
print('This is exercise 8-16')
print()
# I have stored the function make_shirt in a module called shirt_production.py
# I will import the file and call the function using several approaches
# import module_name
import shirt_production


shirt_production.make_shirt('med', 'I like Ike')
print()
# from module_name import function_name
from shirt_production import make_shirt


make_shirt('small', 'Flash')
print()
# from module_name import function_name as fn
from shirt_production import make_shirt as fn


fn('x large', 'I love New York')
print()
# import module_name as mn
import shirt_production as mn


mn.make_shirt('x small', 'Flowers')
print()
# from module_name import *
from shirt_production import *


make_shirt('med', 'Python rules')
print()
# This is exercise 8-17
print('This is exercise 8-17')
print()
print('I have tried to follow the style guidelines for all the exercise that I have done.\
 I double checked exercises 10, 11, and 12. They follow the style guidelines.')
# This is part 2
print('This is Part 2')
print()

# This is exercise 9-10
print('This is exercise 9-10')
print()
import restaurant


my_restaurant = restaurant.Restaurant('Red Lobster', 'Seafood')
my_restaurant.describe_restaurant()
print()

# This is exercise 9-11
print('This is exercise 9-11')
print()
import user_types


my_admin = user_types.Admin('Frank', 'Taplin', 49, 10234, 'Cloud dev')


my_admin.privileges.show_privileges()
print()

# This is exercise 9-12
print('This is exercise 9-12')
print()
import admin_priv

my_admin2 = admin_priv.Admin('Luke', 'Skywalker', 29, 123, 'Jedi')


my_admin2.privileges.show_privileges()
print()

# This is part 3
print('This is Part 3')
print()
# This is exercise 9-16
print('This is exercise 9-16')
print()
print('I went onto python module of the week and looked at the module for strings.\
 It included information about Templates. I\'m going to research how to implement Templates \
 into my coding.')
