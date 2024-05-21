mytuple = ("apple", "banana", "cherry")
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple1,tuple2,tuple3)
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)
print(type(thistuple))
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])
print(type(thistuple[1]))
thistuple = ("apple", "banana", "cherry")
print(thistuple[-3])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[0:7])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[0:7])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[3:])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-4:-0])
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-0])
## convert tuple into the list you can not change the value of tuple but can convert into list.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
x=("bat","ball","cricket")
y=list(x)
y[2]="football"
x=tuple(y)
print(x)

x=("boot","uniform","school")
y=list(x)
y[2]="collage"
x=tuple(y)
print(x)
##tupple changes into list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) 

### remove data in  tupples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
   


#this will raise an error because the tuple no longer exists

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

thistuple=("yash","sagar","bittu")
print(thistuple)

#unpacking  tuple:-- "mens create a tuple and assign new value to it"
fruits = ("apple", "banana", "cherry")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])