# first_name = "Daniel"
# last_name = "Ach"
# age = 21 
# print(f"My name is {first_name} and I am {age} :) ")

# age = int(input("whats your age?"))
# country = input("where are you from ?")
# if age>= 18:
#     print("DRINK DRINK")
# elif age >= 16 and country == "Belgium":
#     print("Ja meneer")
# else:
#     print("nopeeee")


# if condition1 or/and condition2

age = int(input("How old are you? "))
country = input("Where are you from? ")

if age >= 21 and country is not "USA":
	print("Have a beer!")
elif age >= 16 and country == "Belgium":
	print("Have a beer.")
else: 
	print("Have a soda.")
​
​
if country == "USA":
	if age >= 21:
		print("You can have a beer")
	else:
		print("Sorry.")
elif age >= 18:
	print("Have a beer.")
​
​
​
num = int(input("Enter a number: "))
numbers = [1,2,3,4,5]
​
if num in numbers:
	print("Yes, we have your number")
