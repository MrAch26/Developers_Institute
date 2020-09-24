# XP
# EXE 1
class Currency():
    def __init__(self,value,typeC):
        self.value = float(value)
        self.typeC = typeC

    def __repr__(self):
        return f"{self.__class__.__name__} : {self.value}{self.typeC}"
    
    def __str__(self):
        return f"Your currency is = {self.value}{self.typeC}"
    
    def __int__(self):
        return int(self.value)

    def __add__(self,other):
        try :
            if self.typeC == other.typeC:
                return self.value + other.value
            else:
                print("Those aren't same currency ")
        except ValueError:
            raise("{other} must be an int or float ")
            return self.value + other
# CODE OF JOHN
        # def __add__(self, other):
    	# 	if isinstance(other, Currency):
		# 	if self.symbol == other.symbol:
		# 		return Currency(self.value + other.value, self.symbol)
		# 	else:
		# 		raise ValueError("Cannot add different Currency types")
		# else:
		# 	return Currency(self.value + other, self.symbol)


def main():
    dollar = Currency(26,'$')
    shekel = Currency(13, '₪')
 
    print(dollar)
    print(shekel)


if __name__ == "__main__":
    main()
    

	