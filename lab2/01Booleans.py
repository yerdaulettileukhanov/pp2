#Ex1
print(bool("Hello")) #True
print(bool(15)) #True

#Ex2
x = ""
y = 0
z = {}
print(bool(x)) #False
print(bool(y)) #False
print(bool(z)) #False

#Ex3
def myFunction() :
  return True

print(myFunction()) #True

#Ex4
def myFunction() :
  return True

if myFunction():
  print("It's true")
else:
  print("It's false")

#Ex5
x = 200
print(isinstance(x, float)) #False