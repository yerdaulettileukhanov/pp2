#Sets
#Ex1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Ex2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Ex3
thisset = {"apple", "banana", "cherry", True, 1, 2} #1 and True are same, first True will be appear and 1 no

print(thisset)

#Ex4
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Ex5
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access Set Items
#Ex1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Ex2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Add Set Items
#Ex1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Ex2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Ex3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) #type is set yet

#Remove Set Items
#Ex1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #if item does not exist, will raise an error

print(thisset)

#Ex2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #if item does not exist, will NOT raise an error

print(thisset)

#Ex3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Ex4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#Ex5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Loop Sets
#Ex1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
#Ex1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Ex2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Ex3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Ex4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Ex5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Ex6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)