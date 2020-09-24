import time

def timeMe(func):
	
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print("Time: ", end-start)

	return wrapper


@timeMe
def count(n):
	for i in range(n):
		print(i)


@timeMe
def sayHi():
	name = input("What is your name: ")
	print("Hello", name)


@timeMe
def count_shout(end, mult, start=0, word="fizz"):
	for i in range(start, end):
		if i % mult == 0:
			print(word)
		else:
			print(i)