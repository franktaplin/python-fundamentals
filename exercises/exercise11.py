# This is exercise 11
# This is Part 1
print('This is Part 1')
print()
# This is 9-6


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a restaurant that serves {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')


class ICeCreamStand(Restaurant):
    # constructor
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavors = ['Strawberry', 'Cookie Dough', 'Chocolate', 'Vanilla', 'Rocky Road']

    def list_flavors(self):
        print(self.ice_cream_flavors)

    def __str__(self):
        return self.restaurant_name


my_ice_cream = ICeCreamStand('Frosty\'s')
my_ice_cream.describe_restaurant()
my_ice_cream.list_flavors()
print()
# This is Part 2
# This is 9-7
print('This is Part 2')
print()


class User:
    def __init__(self, first_name, last_name, age, student_id, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.major = major

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.student_id)
        print(self.major)

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')


class Admin(User):
    # constructor
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age, student_id, major)
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']

    def show_privileges(self):
        print(f'{self.first_name} {self.last_name}, as an Admin you have the following privileges:')
        for privilege in self.privileges:
            print(f'You {privilege}.')


my_admin = Admin('Frank', 'Taplin', 49, 105312, 'Cloud computing')
my_admin.show_privileges()
print()

# This is Part 3
# This is 9-8
print('This is Part 3')
print()


class User:
    def __init__(self, first_name, last_name, age, student_id, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.major = major

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.student_id)
        print(self.major)

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']

    def show_privileges(self):
        print('As an Admin you have the following privileges:')
        for privilege in self.privileges:
            print(f'You {privilege}.')


class Admin(User):
    # constructor
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age, student_id, major)
        self.privileges = Privileges()


my_admin = Admin('Frank', 'Taplin', 49, 105312, 'Cloud computing')
my_admin.privileges.show_privileges()
print()
# This is Part 4
# This is the horse class from OOP with the 2 child objects.
print('Part 4 is in the version of the horse.py program that is labeled CAC-1040 Inheritance & Polymorphism Lab')
print()
