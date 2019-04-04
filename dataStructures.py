# Dictionaries
squares = {x: x*x for x in range(6)}
print(f'Squares 0-5: {squares}')

# OrderedDict
from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType
d = OrderedDict(one=1, two=2, three=3)
print(f'OrderedDict: {d}')

# Default dicts return the defined value is a key is not found
d = defaultdict(list)
d['dogs'].append('ChouChou')
d['dogs'].append('Retriever')
d['foods'].append('Pizza')
d['foods'].append('Gallo pinto')
print(f'DefaultDict: {d}')

# Chain maps put chains together, ie to search
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
cd = ChainMap(dict1, dict2)
print(f'Chain Map: {cd}')
print(f'Finding three: {cd["three"]}')

# MappingProxyType is for making read-only dicts
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
print(f'Cannot write to MappingProxyType')
try:
    read_only['one'] = 11
except:
    print(f'Write failed. Read only dict: {read_only}')

# Aside from lists, which are dynamically resized, mutable, and contain any items
# of different types
# There are also array.array, which is a type-restricted array, so more efficient
# since more tightly packed

import array
arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(f'Array.array index 1: {arr[1]}')
# Cannot add a diff type
try:
    arr.append('Test')
except:
    print('Failed adding string to float array')


# Byte arrays are mutable:
arr = bytearray((0,1,2,3))
print(f'Byte array: {arr}')
arr[2] = 3
print(f'Byte arrays are mutabble: {arr}')

# Sets and multisets
vowels = {'a','e','i','o','u'}
print(f'Set: {vowels}')
# To create empty set, must use set(), since {} will create empty dict
alice = set('alice')
print(f'Intersection: {alice.intersection(vowels)}')

# Immutable set
vowels = frozenset({'a','e','i','o','u'})
try:
    vowels.append('z')
except:
    print('Cannot add to frozenset')

# Counter: A set, but keep track of occurences
from collections import Counter
inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(f'Inventory: {inventory}')
more_loot = {'bread': 2, 'sword': 2, 'axe': 2}
inventory.update(more_loot)
print(f'Inventory: {inventory}')

# Stacks
# List has O(1) for push and pop. Since lists implemented via dynamic array,
# periodic resizing makes less efficient than others that use linked list
stk = []
stk.append('eat')
stk.append('sleep')
stk.append('code')
print(f'List as stack, pushed 3: {stk}')
popped = stk.pop()
print(f'List stack popped {popped}, remaining: {stk}')

# Deque provides O(1) for either side, so works as queue or stack
from collections import deque
dq = deque()
dq.append('eat')
dq.append('sleep')
dq.append('code')
pl = dq.popleft()
pr = dq.pop()
print(f'Deque, popped left: {pl} Popped right: {pr}. Remaining: {dq}')

# LifoQueue is another stack, but provides locking semantics for concurrent
# produces and consumers
from queue import LifoQueue
lq = LifoQueue()
lq.put('eat')
lq.put('sleep')
lq.put('code')
item = lq.get()
print(f'LifeoQueue, got one: {item}. Remaining: {lq}')