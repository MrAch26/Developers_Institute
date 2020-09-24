
def test(*args):
	print(type(args))
	print(args[4])
	print("printing Args")
	for item in args:
		print(item)

# *  packs items into a tuple, and unpacks into a list
# ** packs items into a dict


def kwtest(**kwargs):
	print(type(kwargs))
	print("printing KWargs")
	for k,v in kwargs.items():
		print(k,"-",v)



def packitup(*args, **kwargs):
	return args, kwargs
	
result = ((1,2,3), {name:"jon", surname:"spiller"})

result[0][2] # 3
result[1]['surname']  # "spiller"