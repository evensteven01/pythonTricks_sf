import functools

def surround_with_me(func):
    def __surround_with_me():
        print('First comes Steve')
        result = func()
        print('Second comes Ford')
        return result
    return __surround_with_me

@surround_with_me
def add():
    return 1+2

def subtract():
    return 2-1

sub_method = surround_with_me(subtract)
res = sub_method()
print(f'Result of {sub_method.__name__}: {res}')

res = add()
print(f'Result of {add.__name__}: {res}')

def absolute_value(func,):
    @functools.wraps(func)
    def __absolute_value(*args, **kwargs):
        """ This converts results to absolute values """
        result = func(*args, **kwargs)
        return abs(result)
    return __absolute_value

@absolute_value
def subtract(a,b):
    """ This is a subtraction method """
    return a-b

res = subtract(1,2)
print(f'Result of {subtract.__name__}: {res} {subtract.__doc__}')
