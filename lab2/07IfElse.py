#Ex1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Ex2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Ex3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Ex4
if a > b: print("a is greater than b")

#Ex5
a = 2
b = 330
print("A") if a > b else print("B")

#Ex6
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Ex7
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Ex8
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement