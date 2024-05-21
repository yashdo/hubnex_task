myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
thisset = {"apple", "banana", "cherry", False, True, 2}

print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# different data type in sets
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
# a sets with the string,int,boolen
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#data type in sets
myset = {"apple", "banana", "cherry"}
print(type(myset))
# note the double round-brackets
thisset = set(("apple", "banana", "cherry")) 
print(thisset)
#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for y in thisset:
  print(y)
  #Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("banana")

print(thisset)
#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

x=thisset.clear()
print(x)
print(thisset)
#The del keyword will delete the set completely:
sagar = {"apple", "banana", "cherry"}
del sagar
print(sagar)
#Loop through the set, and print the values:

yash = {"apple", "banana", "cherry"}

for x in yash:
  print(x)
