"""
28.03.2020
Tuple unpacking
Bogdan Prădatu - Fluent Python
"""

# Tuple unpacking works with any iterable object. The only requirement
# is that the iterable yields exactly one item per variable in the
# receiving tuple, unless you use a star (*) to capture excess items


name = ("Bogdan", "Prădatu")
firstname, lastname = name
print("Firstname:", firstname, "\nLastname:", lastname)

t = (20, 8)
print(divmod(*t))

one, two, *rest = range(5)
print("One:", one)
print("Two:", two)
print("Rest:", rest)

print("\nNested tuple unpacking:\n")
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
