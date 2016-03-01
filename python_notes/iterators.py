# An iteration is taking one of something, one after the other. 
# An iterator is # a Python object that has a __next__ (Python 3) or a next 
# (Python 2) method.
# An iterable is an object that returns an iterator with a __iter__ method or 
# defines a __getitem__ method that accepts valid indexes and raises an
# IndexError if it's not valid. 
#
# So in short, an iterable is something you can get an iterator from. Here's
# an example of an iterator:

# This class only returns the first, third, fifth,  etc. element in the list
# passed.
class Odd:
  def __init__(self, data):
    self.data = data
    self.len = len(self.data)
    self.index = 0
        
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.index >= self.len:
      raise StopIteration
      
    self.index = self.index + 2
    return self.data[self.index-2]

odd = Odd([x for x in range(5)])

# So what iter does is it returns whatever the iterable's __iter__ method returns.
it = iter(odd)

# Should print 0, 2, 4
# I know, it's weird, but 0 is the first element in the sequence given so...
for i in it:
  print(i)
  
odd = Odd('abcdef')
it = iter(odd)

# Should print "a c e"
for i in it:
  print(i)

# This will be an error as you can't reset our Odd iterator!
next(it)

#Keep in mind when you do something like:
it = iter([1,2,3,4,5]) 
# iter simply calls __iter__ of the list class :)
