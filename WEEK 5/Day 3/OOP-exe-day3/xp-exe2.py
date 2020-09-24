class Circle():

    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return Circle.PI * self.radius**2
        
        
# Reading data from a file and making a CSV (Excel file)

# # DATA:
# adam adamson 10
# bobby benson 12
# charlie chaplain 11
# dave davison 9

# CODE #
# with open('secrets.txt', 'r') as f:
# 	data = f.readlines()
# with open('people.csv', 'w') as f:
# 	f.write('First,Last,Age\n')
# 	for line in data:
# 		person = line.split(" ")
# 		f.write(f"{person[0]},{person[1]},{person[2]}")