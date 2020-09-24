# # EXE 1 

# my_fav_numbers = set()
# my_fav_numbers.update([2,6,26,18])
# print(my_fav_numbers)
# my_fav_numbers.add(1)
# my_fav_numbers.add(9)
# print(my_fav_numbers)
# my_fav_numbers.remove(26)
# print(my_fav_numbers)

# friend_fav_numbers={3,4,5,7}
# print("friend_fav_numbers")
# print(friend_fav_numbers)

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers) 

# EXE2
# Its not possible with tuple 

# EXE3
# float = 1.2 = 4.0 = int+decimal
# integer = 1,2,3,4,= int No decimal 

# num={1.2,2.6,3.2}
# print(num)

# ????????

# EXE 4
# for i in range(0,21):
#     print(i)

# # EXE 5
# pizza_toppings = input("What do you want in your pizza ('q' when your are done)")
# list_toppings=[]

# while pizza_toppings.lower().strip() !='q'  :
#     print(pizza_toppings, "was added in your pizza")

#     if pizza_toppings in list_toppings:
#         print("The item is already in the pizz")
#     else :
#         list_toppings.append(pizza_toppings)

#     print(list_toppings)
#     pizza_toppings = input('Anything else ? or quit ')


# EXE 6
# age = int(input("how old are you ?"))
# movie_ticket = 0
# family = ["Daniel","Julien","David"]
# teenager = ["roy","rodey","josef"]
# allowed_ones =[]

# for teen in teenager:
#     age = int(input(f'how old is {teen} ?'))
#     if age >= 21 :
#         allowed_ones.append(teen)
#     else :
#         print("you're not allowed !")

# print(f"{allowed_ones} is/are allowed to enter")

# for member in family:
#     age_family=int(input(f"How old is {member}"))

#     if 3 < age_family <= 12:
#         movie_ticket = movie_ticket + 10

#     elif age_family > 12 :
#         movie_ticket += 15
    
# print(movie_ticket, "total for the family")

# # EXE 7
# users = ["Jose","opaJopa","bili"]
# users_allowed = []

# for user in users :
#     age = int(input(f"How old is {user}"))
    
#     if age > 16 :
#         users_allowed.append(user)
#     print(user)
    

# print(users_allowed, "are in the users")


# # EXE 8
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove('Banana')
# basket.pop()
# basket.append("Kiwi")
# basket.insert(0,'Apples')
# print(basket.count("Apples"),'Apples are in the basket')
# basket.clear()
# print(basket)

# EXE 9 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# pos = len(basket )- 1

# while pos >= 0 :
#     print(basket[pos])
#     pos -= 1


# # EXE 10
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# pos = 0
# # 0 = Banana 1 = wont 2=print 3=not print 4=print 
# while pos < len(basket):
#     if pos % 2 == 0:
#         print(basket[pos])
#     pos += 1 

# EXE 11

# list_a = [num for num in range(3,31,3)]
# print(list_a)

# # EXE 12

# num = None
# for num in range(1500,2701):
#     if num % 7 == 0 and num % 5 == 0:
#         print(num)












