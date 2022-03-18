# This is the module for section 11-3 in exercise13.py
class Employee:
    def __init__(self, first_name, last_name, annual_salary, pay_raise=None):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.pay_raise = pay_raise

    def give_raise(self):
        if self.pay_raise:
            self.annual_salary = self.annual_salary + self.pay_raise
        else:
            self.annual_salary = self.annual_salary + 5000
