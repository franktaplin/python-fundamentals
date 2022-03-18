# This module is for section 9-12 of exercise13.py
import user


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']

    def show_privileges(self):
        print('As an Admin you have the following privileges:')
        for privilege in self.privileges:
            print(f'You {privilege}.')


class Admin(user.User):
    # constructor
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age, student_id, major)
        self.privileges = Privileges()
