#Lists
#Ex1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Ex2
thislist = ["apple", "banana", "aherry"]
print(len(thislist))

#Ex3
a = list(("1", 2, 3.0))
print(a)

#Ex4
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Ex5
list1 = ["abc", 34, True, 40, "male"]
print(list1) #It can hold any values

#Access List Items
#Ex1
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

#Ex2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:4])

#Ex3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Ex4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-3:-1])

#Ex5
thislist = ["apple", "banana", "cherry"]
if "Apple" not in thislist:
  print("Yes, 'Apple' is not in the fruits list")

#Change List Items
#Ex1
thislist = ["apple", "banana", "cherry"]
thislist[-1] = "blackcurrant"
print(thislist)

#Ex2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
print(thislist)

#Ex3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[-3:-1] = ["blackcurrant", "watermelon"]
print(thislist)

#Ex4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.insert(3, "watermelon")
print(thislist)

#Ex5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.insert(-3, "watermelon")
print(thislist) #it will be -4th item

#Add List Items
#Ex1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Ex2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Ex3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Ex4
thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
thislist.extend(tropical)
print(thislist)

#Ex5
thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
tropical.extend(thislist)
print(thislist) #Error

#Remove List Items
#Ex1
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Ex2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Ex3
thislist = ["apple", "banana", "cherry"]
del thislist[0:2]
print(thislist)

#Ex4
thislist = ["apple", "banana", "cherry"]
del thislist #this list doesn't exist

#Ex5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #it is empty list

#Loop Lists
#Ex1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Ex2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Ex3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Ex4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Ex5
thislist = ["apple", "banana", "cherry"]
[print(x, 2) for x in thislist]

#List Comprehension
#Ex1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Ex2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Ex3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#Ex4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [True for x in fruits]

print(newlist)

#Ex5
list = [1, 2, 3, 4, 5]
newlist = [x if x != 2 else "11" for x in list]
print(newlist)

#Sort Lists
#Ex1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Ex2
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Ex3
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Ex4
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Ex5
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Copy Lists
#Ex1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Ex2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Lists
#Ex1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Ex2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Ex3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)