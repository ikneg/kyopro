import itertools

l = ['a', 'b', 'c', 'd']

p = itertools.permutations(l, 2)
print(type(p))
# <class 'itertools.permutations'>