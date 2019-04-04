def foo(req, *args, **kwargs):
    print(f'Required argument: {req}')
    if args:
        print(f'Extra positional arguments: {args}')
    if kwargs:
        print(f'Extra positional arguments: {kwargs}')

foo('ABC')
foo('ABC', 'abc')
foo('ABC', nums='123')
foo('ABC', 'abc', nums='123')
letters = ['a','b']
numbers = {'one': 1, 'two': 2}
foo('ABC', *letters, **numbers)

genexpr = (x for x in range(5))
# Can unpack with * any iterable
print(*genexpr)
print(*numbers)