# This is the horse class form OOP
class Horse:
    # constructor
    def __init__(self, weight, height, sex):
        self._weight = weight
        self._height = height
        self._sex = sex

    # getter property decorators
    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def sex(self):
        return self._sex

    # setter property decorators
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @height.setter
    def height(self, height):
        self._height = height

    @sex.setter
    def sex(self, sex):
        self._sex = sex


my_horse = Horse(400, 80, 'male')
print(my_horse.weight)
print(my_horse.height)
print(my_horse.sex)
