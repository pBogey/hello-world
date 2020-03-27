"""
Named Tuple
16.07.2019
Bogdan Prădatu - Fluent Python
"""

from collections import namedtuple

# Named tuples takes two parameters:
    # class name
    # list of field names
City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)
    # access can be done by name or position
print("population:",tokyo.population)
print("City:",tokyo[0])

print("************************************************************")
LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

class Container:
    __slots__ = ("item1","item2","item3")

    def __init__(self, item1, item2, item3):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3

    def __repr__(self):
        return f"Container(item1={self.item1}, item2={self.item2}, item3={self.item3})"


Recipient = Container(1,2,3)
print("Class:",Recipient)

Container = namedtuple("Container", "item1 item2 item3")
Recipient = Container(1,2,3)
print("NamedTuple:",Recipient)

