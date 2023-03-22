#NamedTuple :Python tuples should be very familiar to everyone. It can store a sequence of Python objects. Unlike list, you can't change the
# value of an element in a tuple. the elements of a tuple are accessed via an index:
'''
Tuple also has a brother named named namedtuple, both of which are tuples, but more powerful.
For namedtuple, you don't have to access it by indexing
 values anymore, you can think of it as a dictionary accessed by name, except that the values
 in it cannot be changed.
'''

from collections import namedtuple
shivu=namedtuple("points","x,y,z")

t1=shivu(10,20,30)
print(t1)
print(t1.y)
print(shivu[t1.x])


