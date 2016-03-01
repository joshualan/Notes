# TODO: Currently a quick and dirty version. Gotta clean it up later.
# Code is also in 2.7

class Parent:
    "This is the docstring"

    # All instances of Parent will share the same instance
    # of shared. Can also be accessed by Parent.shared
    shared = 5

    def __init__(self, name):
        # Both of these attributes will be unique to each
        # instance and will not be shared. However, we imply
        # that age is a hidden variable since it has __ before
        # its name.
        self.name = name
        self.__age = 50

    # All class methods need a reference to self. When we invoke
    # this function, we don't have to pass it though :)
    def scold(self):
        print "Clean your room!"
        self.__age += 1

    def walk(self):
        print "I'm walking 5 m/s."

# We can instantiate a Parent object with its constructor!
p = Parent("Dad")
p.scold()

# There are class names we can invoke

# Prints every attribute and its value
print p.__dict__

# Prints the class name
print p.__class__

# We can inherit classes though!

class Child(Parent):

    # We overrode the __init__ method!
    def __init__(self, name):
        self.name = name
        self.age = 10
        self.toy = "NERF BLASTER"
        print "I'm a kid!"

    def scold(self):
        print "You can't tell me what to do!"
        self.age -= 1

c = Child("Dexter")

# Calling the overridden scold() method
c.scold()

# Calling parent's walk() method
c.walk()


print c.__dict__
print c.__class__
c.walk()

# Quick notes:
# @staticmethod is a decorator we use for class methods that really 
# doesn't use an object at all. Kind of like an addition method for a
# Add class or something
#
# @classmethod is a decorator we use for class methods that are BOUND
# to a class, not an object. Instead of self, we receive a cls. So we can
# do stuff like:

# @classmethod
# def foo(cls):
#   print(cls.bar) # we get the static bar member
#   return cls("hello) # we call the class constructor

# @property and @property.setter
# Decorator for methods. Basically, if an object has the member x and we try
# obj.x, it calls the getter. if we do obj.x = 5, it calls the setter
#
# So we'd do something like
#
# @property
# def x(self):
#   print('I'm in the getter')
#   return self.x
# 
# @x.setter
# def x(self, val):
#   print('I'm in the setter')
#   self.x = val
#
