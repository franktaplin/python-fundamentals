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

    def describe_horse(self):
        print(f'The horse is {self._weight}lbs, {self._height} inches tall, and is a {self._sex}')


class Arabian(Horse):
    # constructor
    def __init__(self, weight, height, sex, mane_length, tail_length):
        super().__init__(weight, height, sex)
        self._mane_length = mane_length
        self._tail_length = tail_length

    # getter property decorators
    @property
    def mane_length(self):
        return self._mane_length

    @property
    def tail_length(self):
        return self._tail_length

    # setter property decorators
    @mane_length.setter
    def mane_length(self, mane_length):
        self._mane_length = mane_length

    @tail_length.setter
    def tail_length(self, tail_length):
        self._tail_length = tail_length

    def describe_horse(self):
        print(f'The Arabian Horse is {self._weight}lbs, {self._height} inches tall, is a {self._sex},')
        print(f'has a {self._mane_length} inch long mane, and a {self._tail_length} inch long tail.')


class Clydesdale(Horse):
    # constructor
    def __init__(self, weight, height, sex, ear_length, neck_length):
        super().__init__(weight, height, sex)
        self._ear_length = ear_length
        self._neck_length = neck_length

    # getter property decorators
    @property
    def ear_length(self):
        return self._ear_length

    @property
    def neck_length(self):
        return self._neck_length

    # setter property decorators
    @ear_length.setter
    def ear_length(self, ear_length):
        self._ear_length = ear_length

    @neck_length.setter
    def neck_length(self, neck_length):
        self._neck_length = neck_length

    def describe_horse(self):
        print(f'The Clydesdale Horse is {self._weight}lbs, {self._height} inches tall, is a {self._sex},')
        print(f'has ears that are {self._ear_length} inches long, and a {self._neck_length} inch long neck.')


my_horse = Horse(400, 80, 'male')
my_horse.describe_horse()
my_arabian = Arabian(500, 78, 'female', 24, 30)
my_arabian.describe_horse()
my_clydesdale = Clydesdale(700, 96, 'male', 12, 28)
my_clydesdale.describe_horse()
