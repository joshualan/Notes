# So the heart of Python is readability. Code is read more often than it is
# written. So basically, when you write code, the goal is to do what you want
# to do in the most readable way.

# General Guidelines

# 1. Explicit is better than implicit

# Bad. It's a way to construct a list but it's way more complicated than it
# should be.
def create_list(x, y, z):
  lst = []
  lst.append(x)
  lst.append(y)
  lst.append(z)
  return lst
  
# Good. We use the [] to create a list and it's pretty clear what you're doing.
def create_list(x, y, z):
  return [x, y, z]
  
# 2. When calling functions, try to follow the positional arguments.

# Best
def create_point(x, y, z):
  return (x, y, z)

point = create_point(1, 2, 3)

# You better have a good reason for doing this..
# This messed with code readability.
point = create_point(z=3,y=2,x=1)

# *args is powerful but can also be unecessary..
def create_point(*args):
  lst = []
  for i in args:
    lst.append(i)
  return tuple(lst)
  
# 3. Don't be an asshole coder. If a data member was specified as private with
# the _member syntax, don't mess around with it. Unlike Java or C++, we let you
# shoot yourself in the foot because we TRUST you as a developer.

# 4. Try to return in only one place. If something went wrong, consider 
# raising an exception instead of returning None or False to indicate incorrect
# input. It's also easier to debug code when there is only one exit point.

# Idioms: How to do stuff the Python Way

# Use enumerate to keep track of where you are
for i, message in enumerate(['hello', 'world']):
  print('Index: {0}, Message: {1}'.format(i,message))
  
# Use list comprehensions!

# Use join on an empty string to make strings!
message = ''.join(['hello', 'world'])
print(message)

# Sets and dictionaries are faster than lists! Sets are pretty much hashtables.
# Lists need to go through each element to figure out if something is in it.

s = set([x for x in range(5)])
l = [x for x in range(5)]

# faster
if 3 in s:
  pass
  
# Slower
if 2 in l:
  pass
  
# Don't check if a variable equals False, None, or 0, just check the variable!

x = None

# Best
if x:
  # do something if true
  pass
else if not x:
  # do something if it's a false value
  pass
else if x is None:
  # do something if None
  pass
  
# Don't use dict.has_key(key), use in or get(key, default_value)
d = {'hello', 'world'}

# Bad
if d.has_key('hi'):
  pass
else
  pass
  
# Good!
if 'hi' in d:
  pass

x = d.get('hi', 'not here')

# Use filter and map! Also, use list comprehensions!

# Bad
lst = [3, 4, 5]
out = []
for i in lst:
  if i != 4:
    out.append(i)
    
# Good
out = [x for i in lst if i != 4]
out = filter(lambda x: x != 4, lst)

# Bad
lst = [3, 4, 5]
out = []

for i in lst:
  out.append(i*50)

# Good
out = [x*50 for x in lst]
out = map(lambda x: x*50, lst)

# Don't use line continuations!

# Open files with WITH
with open('file.txt') as f:
  for line in f:
    pass:
    
