
# ** is the unpacking of a dictionary in Python into key=value.
# That's what kwargs is about.

def foo(**kwargs):
  for k, v in kwargs.items():
    print(k, v)

d = {'q': 'r', 'c': 'd' }

foo(**d)

# is the splat operator. In function prototypes, it's for optional
# unnamed arguments

def bar(x, *args):
  print(x, args)
  
bar(5, 1, 'hi') # prints 5 (1, 'hi') 
