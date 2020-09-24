class Student():
    # MUST START WITH SELF
    def  __init__(self, name, age):
        self.name = name 
        self.age = age

    def sayHi(self):
        print(f'Hello {self.name}')

