# For some reason, git screwed up and the changes I made were never saved.
# I did a pull too and erased my own stuff :( So sad. Here's a super 
# condensed version of this.

# A sequence is an ordered set. We're gonna look at two types of sequences
# in Python: the list and the tuple. The list is pretty great. Every element
# in the list has an index associated with it that you can use to refer to it.
# Lists are also mutable, so you can change their value if they have an index.

l = [1, 2, 3]

l[2] = 4
# Prints out 4
print(l[2])

# So lists are one of the more powerful things you can do in Python. 

# Prints true
print(1 in l)

# inserts 100 in position l[2]
l.insert(2, 100)
print(l)

# Index finds the first position of an element in the list
# Count finds how many times an element appears in the list
# Prints 2 and 1
print(l.index(100), l.count(1))

# del statement removes an item based on index, which is similar to the pop()
# method. remove() deletes an element based on the value passed.
del l[1]
l.remove(100)

# Prints [1, 4] 
print(l)

# Now lists are made even more useful with something called list comprehensions!
# They are an easy way to make lists. They're basically an expression followed by 
# a for clause followed by zero or more for and if clauses.

# Makes a list of squares from 0 to 9:
l = [x**2 for x in range(10)]

# Prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(l)

# Now, let's say we wanted to make a tuple of every odd number below ten raised to
# the power of 1, then 2, and then 3! We would use a more complex list comprehension.

l = [x**y for x in range(10) if x % 2 for y in [1, 2, 3]]

# Prints [1, 1, 1, 3, 9, 27, 5, 25, 125, 7, 49, 343, 9, 81, 729] 
print(l)

# That list comprehension above was basically equal to:
l = []
for x in range(10):
  if x % 2:
    for y in [1, 2, 3]:
      l.append(x**y)
      
# But wait! That isn't a tuple! I guess it's time to use NESTED list comprehensions!
l = [tuple([x**y for y in range(1,4)]) for x in range(10) if x % 2]  

# Prints [(1, 1, 1), (3, 9, 27), (5, 25, 125), (7, 49, 343), (9, 81, 729)] 
print(l)

# Eh? That's pretty cool. That thing was equivalent to:
l = []
for x in range(10):
  tmp = []
  if x % 2:
    for y in range(1,4):
      tmp.append(x**y)
    l.append(tuple(tmp))

# So much simpler! Also, keep in mind that successive for clauses can iterate over
# the vars of the previous clauses. For example:

# What this does is combine the elements of both list. We pretend not to know what
# extend() or + is for this case. 
l = [y for x in [[1, 2, 3], [4, 5, 6]] for y in x]

# Prints [1, 2, 3, 4, 5, 6] 
print(l)

# Tuples are like lists but they're immutable! They also use parentheses instead
# of square brackets. However, a comma-delimited list of things without anything
# around them can also be construed as a tuple.

t = 1, 2, 3

# Prints out 2
print(t[1])

t = (3, 4, 5)

# Prints out 3
print(t[0])

# Once you add a thing to a tuple, you can't change that thing! However, you can
# append to a tuple.

# t[0] = 3 <- NOT ALLOWED
t += 1,
t += 6, 7
t += tuple((8, 9))
# Prints (1, 2, 3, 1, 6, 7, 8, 9) 
print(t)

t = 1, 2

# Assigns 1 and 2 to a and b respectively
a, b = t

# On the other hand, we also have sets! They're unordered (which means they're
# not a sequence) but they cannot contain any duplicate elements. Sets are 
# created using set()! They're equivalent to their 
# mathematical versions. Note that sets are basically hashtables so they're
# pretty fast, faster than using lists!

s = {1, 4, 1, 5}
s2 = {4, 7, 8}

# Prints {1, 4, 5} 
print(s)
# Prints {4} 
print(s & s2)
# Prints {1, 4, 5, 7, 8} 
print(s | s2)
# Prints {1, 5} 
print(s - s2)

# You can add individual elements to a set using add or add a list of 
# them using update!

s.update((3,20))
s.add(17)
# Prints {1, 3, 4, 5, 17, 20} 
print(s)

# You can remove an element from a set using remove()
s.remove(20)
# Print {1, 3, 4, 5, 17} 
print(s)

# You can also do set comprehensions!
x = {x for x in range(10) if x % 2}

# Prints set of odd numbers {1, 9, 3, 5, 7} 
print(x)

# Dictionaries are basically maps or tables in Python. You instantiate
# one using {} or dict() or even dictionary comprehensions!

# These are equivalent 
d = { 'good': 'star wars', 'meh': 'star trek', 'shots': 'fired' }
d = dict([('good', 'star wars'), ('meh': 'star trek'), ('shots', 'fired')])

# Prints 'star trek'
print(d['meh']) 

# Dict comprehension of 10 numbers numbers to their squares:
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} 
d = {x: x**2 for x in range(10)}

# Use in to figure out if a key is in the dictionary
# Prints False
print('LOTR' in d)

# Use del to remove a key value pair
del d[9]

# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 
print d

# dict.keys() returns a dict_keys object which is an iterable of the
# dictionary's keys but with no indexing. You can easily turn it into 
# a list though.

# Prints [0, 1, 2, 3, 4, 5, 6, 7, 8] 
print(list(d.keys()))
