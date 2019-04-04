# __str__ gets called on object whenever try to convert object to string

class Man:
    name = 'Steve'
    age = 36

    def __str__(self):
        return f'Name: {self.name} Age: {self.age}'

    def __repr__(self):
        return f'__repr__<Man object name: {self.name} age: {self.age}>'

steve = Man()
print(steve)
print(str(steve))
print(repr(steve))
bob = Man()
bob.name = 'Bobb'
bob.age = 53

men = [steve, bob]
# Printing containers always uses __repr__
print(men)

# __str__ is human-readable, and acceptable to show to user
# __repr__ is unamiguous above all, debugging aid

import datetime
today = datetime.date.today()
print(str(today))
# With repr you see full module and class name. Can even copy paste to recreate object
# This is a good goal
print(repr(today))

# In python3, all strings are unicode
# In python2, there are two: str (ASCII), and unicode
# Python2 __str__ returns bytes, __unicode__ returns characters