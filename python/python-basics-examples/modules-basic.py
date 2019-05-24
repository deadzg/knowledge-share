'''
What are modules? -> objects of type ModuleType






How modules are loaded?
How to import without import statements?
Reloading modules
Import variants
__main__
zip archives
packages
implicit namespace packages (>3.3)
'''

# Standard libraries are written in python
# Built-in libraries are written in C
import math
import pprint

print (math)
print (type(globals()))
print ()
print (globals()['math'])
import fractions

import math

# It will not create another object. These are singleton objects
# Ref is added to system cache as well

print (fractions)

junk = math

print (junk.sqrt(2))
print (junk is math)
print ('************* \n\n\n\n')

import sys

print (sys.modules['math'])
print (id(sys.modules['math']))


print (math.__name__)
print (math.__dict__)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(math.__dict__)
pp.pprint(fractions.__dict__)
print ('$$$$$$$$$$$$$$$$$$$$$$$$')
print (math.__dict__['sqrt'])



def func():
    a = 10
    return a

print(func)
print(func())
print(id(func))
print(globals())
print(globals()['func']())

# Name spaces are dictionary

print (locals())

def func2():
    a = 10
    b = 20
    print (locals())

func2()    


