# This module is for section 9-12 of exercise13.py
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
