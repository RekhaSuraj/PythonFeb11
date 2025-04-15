d1 = {1:'cat',2:'dog',3:'goat',4:'sheep',5:'cow'}

# pop() - remove specified key and return the associated value.
# syntax : pop(key)
print(d1.pop(2))
# dog

print(d1)
# {1: 'cat', 3: 'goat', 4: 'sheep', 5: 'cow'}


# popitem(self, /)
#     Remove and return a (key, value) pair as a 2-tuple.
#
#     Pairs are returned in LIFO (last-in, first-out) order.
#     Raises KeyError if the dict is empty.
# print(help(dict.popitem))

d1.popitem()
print(d1)
# {1: 'cat', 3: 'goat', 4: 'sheep'}

d1.popitem()
print(d1)
# {1: 'cat', 3: 'goat'}


