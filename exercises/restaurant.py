# This is the Restaurant class for section 9-10 of exercise13.py


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a restaurant that serves {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')
