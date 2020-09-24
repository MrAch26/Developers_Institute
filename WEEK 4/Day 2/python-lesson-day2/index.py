Notes from today:
12 h 36
text = None
while text != "q":
	text = input("Enter a letter (q to quit): ")
	print("You entered", text)
print("goodbye")
#infinite loops:
while True:
	print("looping...")   #ctrl + c
for i in range(1000000):
	if i == 10:
		break
	print(i)
for i in range(20):
	if i == 10:
		continue
	print(i)
12 h 36x

Sequences: Start at 0. Not at 1.
# Strings
name = "Jonathan"
# Lists
names = ["Adam", "Bob", "Charlie"]
names[-1]  # Charlie
# Set
emails = {"a@a.com", "b@b.com", "c@c.com"}
# Tuple
days = (
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
)
# Dictionary
salaries = {
	"Dave": 20000,
	"Eddy": 30000,
	"Freddy": 5000
}
# Slicing
# [start:stop:step]
# Start is inclusive, Stop is exclusive
# append() - adds to the end
# remove(VALUE) - removes an item
# pop() - removes from index or end
# index(VALUE) - returns the index where
# 				 the value is found
# How do you add to the left side of the array?
# How do you add in the middle of the array?
# MUTABILITY  - Ability to be changed
# a list is mutable
# list1 = [5, 10, 15, 20, 25, 50, 20]
# if 20 in list1:
# 	list1[list1.index(20)] = 200
# Set is a bunch of items WITH NO DUPLICATES
# Sets are NOT ordered.  And therefor NOT indexable.
# Tuples are like immutable lists.
# tup = (1,2,3)
# Structure and operations that
# become more complex with size.
# insert(600)
# Dictionary... no matter how big they get.
# Operations on them are still instant.
basket = ['apple', 'banana', 'kiwi', 'pear']
for fruit in basket:
	print(fruit)

list[::-1]
range(start, stop, step)   stop is exclusive

Iterable
it can be iterated over
iteration... counting.
Mutable, iterable
Range works very similarly to slicing...
range(stop[, start=0, step=1])
range(100)  #stop
range(1,100)  #start, stop
range(1,100,2) #start, stop, step
range(stop=100,step=2)
Why do we start counting at 0
and why is "stop" exclusive?