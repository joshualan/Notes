# Note: Read iterators.py before this because you need to understand
# iterables to truly understand generators. Or not because I'm not 
# the police.

# So a generator is a function that returns an object that you can
# call next on! Every call to next() returns a value and eventually,
# a StopIteration exception will be raised to show that no more values
# can be returned.

# So functions usually use "return" but generators use yield. This is
# the piece that turns a function into a generator. 

def foo(n):
  yield n % 2
  yield n % 3

gen = foo(7)

# Should print out "1 1" since 7 % 2 and 7 % 3 are both 1.
for i in gen:
  print(i)

# Generators are like iterators and cannot be restarted!
gen = foo(8)

# Should print out 0
print(next(gen))

# Should print out 2
print(next(gen))

# Should raise a StopIteration exception 
#print(next(gen))

# So in essence, a generator is an alternate, faster, and less memory-
# intesive way of implementing the iterator protocol!

# We can also do something called generator expressions!

gen = (x*x for x in range(10))

# This prints the squares of the numbers 0 to 9
for i in gen:
  print(i)
  
# Generator expressions can get pretty complex!

def unique(iterable, key=lambda x: x):
    seen = set()
    for elem, ekey in ((e, key(e)) for e in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)
            
# This function yields a set of unique values based on the elements
# in the iterable passed with the function passed in applied to them.
# We use a generator to iterate through the iterable as well!

# Generators don't even have to necessarily end!
# We can simply stop calling the function if we wanted!

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

# Another note is that we can call the send() function of a generator!
# This allows us to both receive a value yielded from the generator and 
# also receive a value from it. This is kind of reminds me of multi-
# threaded programming. We can yield nothing and also send None.

def quick_example():
  data = yield
  yield sum(data)

# Readings: 
#
# Generator Expressions Abstract: https://www.python.org/dev/peps/pep-0289/
# Yield and Generators Explained: https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
