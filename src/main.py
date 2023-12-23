class RealCollisionObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        # A simple hash function that uses the length of the input string.
        return len(self.value)


# Create a dictionary and insert objects with potential hash collisions
dictionary = {}
obj1 = RealCollisionObject("apple")
obj2 = RealCollisionObject("orang")

# Both objects have the same hash value (length of the string), potentially leading to a collision
dictionary[obj1] = "fruit 1"
dictionary[obj2] = "fruit 2"

print(dictionary[obj1])
print(dictionary[obj2])
