"""
Functional programming with python
14.08.2019
Bogdan Prădatu - Fluent Python
"""

from functools import reduce

def fact(n):
    return reduce(lambda a,b: a*b, range(1, n+1))

print("fact(5):",fact(5))

from operator import mul

def fact(n):
    return reduce(mul, range(1, n+1))

print("fact(5):",fact(5))

print("\n**********          Itemgetter          ***********\n")

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

# itemgetter(1) does the same as lambda fields: fields[1]
# create a function that, given a collection, returns the item at index 1.
from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
print('\n')
cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))

print("\n**********          Attrgetter          ***********\n")
from collections import namedtuple
LatLong = namedtuple('Latlong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat,long))
               for name, cc, pop, (lat,long) in metro_data]

print("metro_areas[0]:",metro_areas[0])
print("metro_areas[0].coord.lat:",metro_areas[0].coord.lat)
print('\n')
from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

print("\n**********          Methodcaller          ***********\n")
from operator import methodcaller
s = "The time has come"
upcase = methodcaller('upper')
print("upcase(s):",upcase(s))
hiphenate = methodcaller('replace', ' ', '-')
print("hiphenate(s):",hiphenate(s))
