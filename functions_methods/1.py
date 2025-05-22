"""
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
"""

# we get an error because we are trying to print foo but it is in the scope of the set_foo function so we can't access it