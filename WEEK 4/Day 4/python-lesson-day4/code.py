
#our implementation of square function

def mysquare(nums):
	'''
	Squares a list of numbers

	args: nums list
	return: list

	'''
	squares = []
	for num in nums:
		squares.append(num**2)
	return squares

original = [1,2,3]
squares = mysquare(original)  # [1,4,9]


# map: takes a list and applies a function to every item in that list
# and then returns the resulting list.


def square(n):
	return n**2

squares = list(map(square, [1,2,3,4,5]))


def even(n):
	if n % 2 == 0:
		return True
	return False

answer = list(filter(even, [1,2,3,4,5,6])) #[2,4,6]


# map, filter, reduce
# loop over an array(list) and do something



