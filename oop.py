# Classes vs instance variables

class Car:
    color = 'Red' # this is an class variable

    def __init__(self, name):
        self.name = name # This is an instance variable

my_car = Car('My car')
other_car = Car('Other car')
other_car.color = 'Blue'
print(f'My car color: {my_car.color} Other car color: {other_car.color}')
# Result: My car color: Red Other car color: Blue
Car.color = 'Orange'
print(f'My car color: {my_car.color} Other car color: {other_car.color}')
# Result: My car color: Orange Other car color: Blue
# By doing other_car.color, we created a instance variable with the same name as
# the class variable, and hence ended up shadowing/overriding and hiding the
# class variable

# You can access class variables from an instance variable.
# IE to keep track of instances of a class:
class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

print(f'{CountedObject.num_instances} insantiations of CountedObject')
co1 = CountedObject()
print(f'{CountedObject.num_instances} insantiations of CountedObject')
co2 = CountedObject()
print(f'{CountedObject.num_instances} insantiations of CountedObject')

# Class vs instance vs static methods
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

mc = MyClass()
print(mc.method())
# You can also do:
print(MyClass.method(mc))

print(mc.classmethod())
print(MyClass.classmethod())

print(mc.staticmethod())
print(MyClass.staticmethod())

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    # These are class methods that are useful as factory functions
    @classmethod
    def margherita(cls):
        # Its better to use cls here instead of Pizza to follow DRY, and makes easier
        # to later change the class name more easily
        return cls(['mozzarella', 'tomatoes'])

    #Class factory methods are in a way a method to add constructors to a class
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

print(Pizza.margherita())