#python variables section
#ex1
x = 5
y = "John"
print(x)
print(y)

#ex2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#ex3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#ex4
x = 5
y = "John"
print(type(x))
print(type(y))

#ex5
x = "John"
# is the same as
x = 'John'

#ex 6
a = 4
A = "Sally"
#A will not overwrite a

#variable names section
#ex1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#ex2, error
2myvar = "John"
my-var = "John"
my var = "John"

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#assign multiple values section
#ex1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#ex2
x = y = z = "Orange"
print(x)
print(y)
print(z)

#ex3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables section
#ex1
x = "Python is awesome"
print(x)

#ex2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#ex3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#ex4
x = 5
y = 10
print(x + y)

#ex5, error
x = 5
y = "John"
print(x + y)

#ex6
x = 5
y = "John"
print(x, y)

#global variables section
#ex1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#ex2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#ex3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#ex4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)