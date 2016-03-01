# Modules are one of the best and most natural ways to structure your code.
# They are an abstraction layer, which means we can separate code into parts 
# that have related functionality or data. They're pretty easy to grasp, which 
# means that it's also really easy to screw up. 

# Here's some things that we should try to avoid:
# 1. Messy, circular dependencies. If class Spaceship needs to import Scotty
# to implement Spaceship.hullIntegrity() and Scotty needs to import Spaceship
# to answer Scotty.isHappy(), then it's a circular dependency.
#
# 2. Relying too much on global state or context. These can be changed by
# literally anything! Try to explicitly pass things that we depend on.
#
# 3. Spaghetti code. This means that our program has complicated flow, 
# redundant code, and basically not understandable.
#
# 4. Ravioli code. This means we have a lot of very similar code in a lot
# of places. In an overzealous attempt to encapsulate and loosely couple code,
# foo() calls 5 other functions to access bar when once can import bar instead.
# Remember kids: simple > complex > complicated

# Now for example, let's use the collections's defaultdict as an example
import collections *
names = defaultdict(int)

# This means the interpreter will look for collections.py in the current path
# and throw an ImportError exception if iti doesn't exist. It also runs any
# top level statements in collections.py However, this example is bad
# though. Is defaultdict() part of collections? Is it a local function? This
# made code hard to read and blurred the lines between dependencies.

from collections import defaultdict
names = defaultdict(int)

# This is slightly better. It shows where defaultdict is coming from.

import collections
names = collections.defaultdict(int)

# This is pretty good. Though the from example was pretty terse, dozens of
# similar from mod import func will make it hard to read. This example
# makes it pretty clear where defaultdict is coming from, no matter how
# many imports.

# Packages are simply modules++. A directory is considered a package if it
# contains an __init__.py. This file's top-level statements will be ran when
# we try to import the package. For example, import pack.modu means we're gonna
# look for a directory called pack, run __init__.py's top level statements,
# find modu.py and run its top-level statements. __init__.py is good for keeping
# all package-wide definitions together. 
