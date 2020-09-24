# We have complex variables such as: List, Dict.
# We can create our own complex variables by defining new classes.

class Student():

	def __init__(self, name, age, courses={}):
		self.name = name
		self.age = age
		self.courses = courses

	def sayHi(self):
		print(f"Hello my name is {self.name} and I am {self.age} years old")

	def haveBirthday(self):
		print("Happy Birthday")
		self.age += 1

	def register(self, course_name, previous_grade=None):
		self.courses[course_name] = previous_grade
		print(f"You just registered for {course_name}")



class Text():

	def __init__(self, value):
		self.value = value

	def upper(self):
		uppertext = ""
		for letter in self.value:
			uppertext += chr(ord(letter) - 32)
		return  uppertext

	def lower(self):
		lowertext = ""
		for letter in self.value:
			lowertext += chr(ord(letter) + 32)
		return  lowertext

	def capitalize(self):
		return self.upper()[0] + self.value[1:]