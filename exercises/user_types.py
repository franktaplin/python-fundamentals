# This module is for section 9-11 of exercise13.py


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
