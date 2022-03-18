# This is Exercise 14
# This is Part 1
# Section 11-1
print('This is Part 1')
print()
import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    # test case for city_functions.py

    def test_city_country(self):
        city_country_test = city_country('santiago', 'chile')
        self.assertEqual(city_country_test, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
# This is Part 2
# Section 11-2
print('This is Part 2')
print()
import unittest
from city_function2 import city_country


class CityTestCase(unittest.TestCase):
    # test case for city_functions.py

    def test_city_country(self):
        city_country_test = city_country('santiago', 'chile')
        self.assertEqual(city_country_test, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country_population_test = city_country('santiago', 'chile', 'population=50000')
        self.assertEqual(city_country_population_test, 'Santiago, Chile - Population=50000')


if __name__ == '__main__':
    unittest.main()
# This is Part 3
# Section 11-3
print('This is Part 3')
print()
import unittest
from employee import Employee


class TestEmployeeCase(unittest.TestCase):
    # Test case for Employee class

    def setUp(self):
        # create test employee
        self.test_my_employee = Employee('Frank', 'Taplin', 50000)

    def test_give_default_raise(self):
        # test to see if standard pay raise is given
        self.test_my_employee.give_raise()
        self.assertEqual(self.test_my_employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        # test to see if custom pay raise is given
        self.test_my_employee.pay_raise = 3500
        self.test_my_employee.give_raise()
        self.assertEqual(self.test_my_employee.annual_salary, 53500)


if __name__ == '__main__':
    unittest.main()
