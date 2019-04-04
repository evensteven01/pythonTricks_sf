# Difference between equal and identical

# == compares equality (same contents)

# 'is' compares identity (point to same identical object)

a = [1,2,3]
b = a

print(a==b)
# True, look the same
print(a is b)
# Also true because point to same object

b = list(a)
print(a==b)
# True, look the same
print(a is b)
# False because we created a new copy

b = [1,2,3]
print(a==b)
# True, look the same
print(a is b)
# False because we assigned to new list object