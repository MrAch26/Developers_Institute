class Secret:

	def __init__(self, password, admin=False):
		self.unsecure_password = password   #this can be viewed and changed in any way.
		self.__password = password   #this can only be viewed and changed according to our rules
		self.admin = admin
	
	
	@property
	def password(self):   
		if self.admin:
			return self.__password
		else:
			return "*"*len(self.__password)


	@password.setter
	def password(self, new_password):
		if not self.admin:
			raise ValueError("Sorry, you're not an admin")

		if len(new_password)< 6:
			raise ValueError("Password must be at least 6 chars")

		self.__password = new_password