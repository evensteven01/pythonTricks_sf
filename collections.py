# Named tuples are extension to tuple, and way to more quickly define a class
# Good way to think of them is memory efficient shortcut to define immutabble class

from collections import namedtuple
import json

Car = namedtuple('Car', ['color', 'mileage'])
my_car = Car('grey','6000')
print(my_car)
print(f'Color of my car: {my_car.color}')

# Named tuples are still immutabble:
try:
    my_car.color = 'red'
except AttributeError as err:
    print(f'Error: {err}')

# Can do other operations valid to tuples:
color, mileage = my_car
print(color,mileage)

# Helpful functions
print(f'My car as dict: {my_car._asdict()}')
print(json.dumps(my_car._asdict()))
# Then to json: