#Tuples
#Ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Ex2
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Ex3, tuple
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple, string
thistuple = ("apple")
print(type(thistuple))

#Ex4
tuple1 = ("abc", 34, True, 40, "male")

#Ex5
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Access Tuple Items
#Ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Ex2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Ex3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Ex4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Ex5
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Update Tuples
#Ex1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Ex2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Ex3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Ex4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Ex5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Unpack Tuples
#Ex1
fruits = ("apple", "banana", "cherry") #packing

#Ex2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits #unpacking

print(green)
print(yellow)
print(red)

#Ex3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Ex4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop Tuples
#Ex1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Ex2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Ex3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuples
#Ex1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Ex2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Ex3
t = (1, 3, 4, 7)
a = t.index(3)
print(a) #finds 3's first appereance index - 1