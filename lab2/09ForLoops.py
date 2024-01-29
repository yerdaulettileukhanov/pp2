#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Ex2
for x in "banana":
  print(x)

#Ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Ex5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Ex6
for x in range(6):
  print(x)
else:
  print("Finally finished!")