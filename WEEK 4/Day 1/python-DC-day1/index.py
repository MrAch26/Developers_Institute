# DAILY CHALLENGE:
text = input("Enter some stuff (10 characters max): ")  #JonathanSp
print("First and Last:")
print("first:", text[0])
print("last:", text[-1])
print("Build Up")
for i in range(len(text)):
	print(text[0:i+1])
print("jumbled")
new_text = ""
#Method1
# new_text += text[::-2]
# new_text += text[::2]
#Method2
from random import randint
for i in range(10):
	new_text += text[randint(0,10)]
print(new_text)
















