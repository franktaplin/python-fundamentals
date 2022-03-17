# This is the guitar class form OOP
class Guitar:
    # constructor
    def __init__(self, body_material, weight, length):
        self._body_material = body_material
        self._weight = weight
        self._length = length

    # getter property decorators
    @property
    def body_material(self):
        return self._body_material

    @property
    def weight(self):
        return self._weight

    @property
    def length(self):
        return self._length

    # setter property decorators
    @body_material.setter
    def body_material(self, material):
        self._body_material = material

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @length.setter
    def length(self, length):
        self._length = length


my_guitar = Guitar('wood', 10, 36)
print(my_guitar.body_material)
print(my_guitar.weight)
print(my_guitar.length)