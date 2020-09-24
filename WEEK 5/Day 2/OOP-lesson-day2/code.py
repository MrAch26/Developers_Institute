class Animal():

	id = "Animal"

	def __init__(self, name, sound):
		self.name = name
		self.sound = sound

	def greet(self):
		print(f"Hi, my name is {self.name}")

	def talk(self):
		print(self.sound * 3)



class Dog(Animal):

	id = "Dog"

	def __init__(self, name, sound, owner):
		super().__init__(name, sound)
		self.owner = owner

	def play(self):
		print("I am playing fetch")

	def home(self):
		print(f"I'm going back to {self.owner}")

	def greet(self):
		print(f"I'm wagging my tail")


def sayHi(any_animal):
	any_animal.greet()


# class Payment():

# 	balance

# 	def pay(amount):
# 		balance -= amount
# 		return amount

# class Cash(Payment):
# 	pass

# class Credit(Payment):
# 	pass

# class Bitcoin(Payment):
# 	pass


# def makePayment(payment_type, amount):
# 	payment_type.pay(amount)





class Shape():
	def __init__(self, name):
		self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        Shape.__init__(self, name)
        self.radius = radius



class Bank():
	def __init__(self):
		self.__balance = 0
		self.__overdraft = 100

	def deposit(self, amount):   #setter
		if amount > 10000:
			print("Calling the tax authority")
		self.__balance += amount

	def view_statement(self):  #getter
		print("Your balance: ", self.__balance)


	def set_overdraft(self, amount):
		self.__overdraft += amount

	def get_overdraft(self):
		return self.__overdraft