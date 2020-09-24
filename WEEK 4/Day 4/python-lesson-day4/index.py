def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

def mul_list(lst):
    if not lst:
        return 0

    total = 1
    for num in lst:
        total *= num
    return total


A couple of functions and algorithms:
def sum_list(thelist):
	total = 0
	for num in thelist:
		total += num
	return total
def mult_list(thelist):
	if not thelist:
		return 0
	total = 1
	for num in thelist:
		total *= num
	return total