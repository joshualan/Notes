# So in essence, a decorator is a function that adds functionality to another
# function.

import time

def outer(func):
  
    def inner():
        print("I'm in a decorator")
        func()
        print("I'm leaving a decorator")
    
    return inner
        
def papyrus():
  print("I'm a cool dude")
  

papyrus = outer(papyrus)

inner()


# In this example, we've effectively *decorated* papyrus() to print out a string
# before you enter it and a string after it!

# An alternative is using the @ syntax

@outer
def sans():
  print("It's a nice day outside.")
  
sans()

# In this one, when we refer to sans(), we actually call outer(sans)!
# This is super useful for setting up stuff to run before a function or adding
# functionality to a function without changing the original function's definition.

def timer(func):
  
  def wrapper():
    start = time.time()
    func()
    end = time.time()
    
    print("This function took {} seconds to run!".format(end-start))
    
  return wrapper

@timer  
def foo():
  sum = 0
  for i in list([1, 2, 3, 4, 5] * 100):
    sum += i**2
  
foo()

# In this example, we decorated foo() to time how long it ran!
