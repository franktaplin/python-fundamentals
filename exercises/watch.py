# This is the watch class from OOP
class Watch:
    # constructor
    def __init__(self, weight, face_material, body_material):
        self._weight = weight
        self._face_material = face_material
        self._body_material = body_material

    # get for weight
    def get_weight(self):
        return self._weight

    # set for weight
    def set_weight(self, weight):
        self._weight = weight

    # get face material
    def get_face_material(self):
        return self._face_material

    # set for face material
    def set_face_material(self, face_mat):
        self._face_material = face_mat

    # get for body material
    def get_body_material(self):
        return self._body_material

    # set for body material
    def set_body_material(self, body_mat):
        self._body_material = body_mat

    # creating properties for attributes
    weight = property(get_weight, set_weight)
    face_material = property(get_face_material, set_face_material)
    body_material = property(get_body_material, set_body_material)


# create instance
my_watch = Watch(5, 'crystal', 'plastic')

# test getter
print(my_watch.get_weight())
print(my_watch.get_face_material())
print(my_watch.get_body_material())
