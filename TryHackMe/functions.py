"""
As programs start to get bigger and more complex, some of your code will be repetitive, writing the same code to do the same calculations, and this is where functions come in. A function is a block of code that can be called at different places in your program.

You could have a function to work out a calculation such as the distance between two points on a map or output formatted text based on certain conditions. Having functions removes repetitive code, as the function's purpose can be used multiple times throughout a program.
"""
def sayHello(name):
     print("Hello " + name + "! Nice to meet you.")

sayHello("ben") # Output is: Hello Ben! Nice to meet you

"""
 Similar to if statements, anything after the colons that is indented is considered part of the function.

A function can also return a result, see the code block below:
"""
def calcCost(item):
     if(item == "sweets"):
          return 3.99
     elif (item == "oranges"):
          return 1.99
     else:
          return 0.99

spent = 10
spent = spent + calcCost("sweets")
print("You have spent:" + str(spent))
