# This is the boat class from OOP
class Boat:
    # constructor
    def __init__(self, depth, keel_length, hull_material):
        self._draft_depth = depth
        self._keel_length = keel_length
        self._hull_material = hull_material

    # get for draft depth
    def get_draft_depth(self):
        return self._draft_depth

    # set for draft depth
    def set_draft_depth(self, depth):
        self._draft_depth = depth

    # get for keel length
    def get_keel_length(self):
        return self._keel_length

    # set for keel length
    def set_keel_length(self, length):
        self._keel_length = length

    # get for hull material
    def get_hull_material(self):
        return self._hull_material

    # set for hull material
    def set_hull_material(self, material):
        self._hull_material = material

    # creating properties for attributes
    draft_depth = property(get_draft_depth, set_draft_depth)
    keel_length = property(get_keel_length, set_keel_length)
    hull_material = property(get_hull_material, set_hull_material)


# create instance
my_boat = Boat(32, 120, 'fiberglass')

# test getter
print(my_boat.get_draft_depth())
print(my_boat.get_keel_length())
print(my_boat.get_hull_material())


