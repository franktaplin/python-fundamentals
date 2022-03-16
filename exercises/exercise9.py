# This is Part 1
print('This is Part 1')
print()
# This is exercise 8-3
print('This is exercise 8-3')
print()


def make_shirt(size, text):
    print(f'The shirt is size {size} and the text on it is "{text}".')


make_shirt('med', 'I like Ike')
make_shirt(size='small', text='I love New York')


# This is exercise 8-4
print('This is exercise 8-4')
print()


def make_shirt2(size='large', text='I love Python'):
    print(f'The shirt is size {size} and the text on it is "{text}".')


make_shirt2()


make_shirt2(size='med', text='C# rocks')


print()
# This is exercise 8-5
print('This is exercise 8-5')
print()


def describe_city(city_name, country_name='USA'):
    print(f'{city_name} is in {country_name}.')


describe_city('New York')
describe_city('Portland')
describe_city('London', country_name='England')

# This is Part 2
print('This is Part 2')
print()
# This is exercise 8-9
print('This is exercise 8-9')
print()
text_messages = ['Hello', 'Good bye', "See ya"]


def show_messages(arg_message):
    for arg in arg_message:
        print(arg)


show_messages(text_messages)
print()
# This is exercise 8-10
print('This is exercise 8-10')
print()
sent_messages = []


def send_messages(new_message):
    for new in new_message:
        print(new)
        sent_messages.append(new)


send_messages(text_messages)
print(text_messages)
print(sent_messages)
print()
# This is exercise 8-11
print('This is exercise 8-11')
print()


send_messages(text_messages[:])
print(text_messages)
print(sent_messages)
print()

# This is Part 3
print('This is Part 3')
print()
# This is exercise 9-1
print('This is exercise 9-1')
print()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')


restaurant = Restaurant('Frank\'s Place', 'Chinese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
# This is exercise 9-2
print('This is exercise 9-2')
print()
restaurant1 = Restaurant('Bubba\'s', 'American')
restaurant2 = Restaurant('Mabels', 'Southern')
restaurant3 = Restaurant('Playa Azul', 'Mexican')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
print()
# This is exercise 9-3
print('This is exercise 9-3')
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


user1 = User('Frank', 'Taplin', 49, 501002, 'Cloud')
user2 = User('Rhonda', 'Williams', 47, 105207, 'Social Work')
user3 = User('Katlyn', 'Williams', 20, 133045, 'IT')
user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()
print()
# This is Part 4
print('This is Part 4')
print()
# This is exercise 9-4
print('This is exercise 9-4')
print()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')

    def set_number_served(self, cust_served):
        self.number_served = cust_served
        print(f'{self.number_served} customers have been served.')

    def increment_number_served(self, daily_cust):
        self.number_served += daily_cust
        print(f'{restaurant.number_served} customers have been served.')


restaurant = Restaurant('Frank\'s Place', 'Chinese')
print(f'{restaurant.number_served} customers have been served.')
restaurant.number_served = 23
print(f'{restaurant.number_served} customers have been served.')
restaurant.set_number_served(15)
restaurant.increment_number_served(12)
print()
# This is exercise 9-5
print('This is exercise 9-5')
print()


class User:
    def __init__(self, first_name, last_name, age, student_id, major, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.student_id)
        print(self.major)

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Frank', 'Taplin', 49, 501002, 'Cloud', 0)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f'There have been {user1.login_attempts} login attempts.')
user1.reset_login_attempts()
print(f'There have been {user1.login_attempts} login attempts.')
