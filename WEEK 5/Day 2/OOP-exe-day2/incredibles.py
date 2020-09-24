from main import Family

family_dict=[{
    'name':'Bob',
    'age':40,
    'gender':'Male',
    'power':'SuperHuman Strength',
    'incredible_name':'Mr. Incredible'
},{
    'name':'Helen',
    'age':40,
    'gender':'Female',
    'power':'Elasticity',
    'incredible_name':'Elastigirl'
},{
    'name':'Violet',
    'age':16,
    'gender':'Female',
    'power':'Invisibility',
    'incredible_name':'InvisibleGirl'
},{
    'name':'Dash',
    'age':12,
    'gender':'Male',
    'power':'SuperFastSpeed',
    'incredible_name':'Speedster'
}
]

class TheIncredibles(Family):
    def __init__(self,last_name,members=[]):
        super().__init__(last_name,members)
    
    def use_power(self, name):
        try :
           for i in range(len(self.members)):
                if self.members[i]['name'] == name:
                    if self.members[i]['age'] >= 18:
                        print(self.members[i]['power'])
                    else:
                        print('The member is under-age') 
        except:
            print('Error')
       
    def __repr1__(self):
        output = [self.last_name]
        for member in self.members:
            output.append(f"name: {member['incredible_name']}, age: {member['age']}, gender: {member['gender']}")
        return "\n".join(output)    

        # if self.is_child_18(name) == True: -- using self.method from parent 
        #     for i in range(len(self.members)):
        #         if self.members[i]["name"] == name:
        #             print(self.members[i]["power"])
                           
    # def __repr__(self):
    #     output = [self.last_name]
    #     for member in self.members:
    #         output.append(f"name: {member['name']}, age: {member['age']}, gender: {member['gender']}")
    #     return "\n".join(output) 
    def presentHeroes(self):
        print("Welcome The Heroes!")
        output = [self.last_name]
        for member in self.members:
            output.append(f"name: {member['incredible_name']}, age: {member['age']}, power: {member['power']}")
        print ("\n".join(output))



def main():
    # print("Hello")
    the_incredibles = TheIncredibles("The Parr Family",family_dict)
    # print(the_incredibles.last_name)
    
    # the_incredibles.use_power('Helen')
    # the_incredibles.use_power('Dash')
    
    the_incredibles.born(name='JackJack',age=1,gender='Male',power='UNKNOWN',incredible_name='BabyJack Incredible')
    # print(the_incredibles.members)
    print(the_incredibles,'\n') #don't need the 
    the_incredibles.presentHeroes()
    
if __name__ == '__main__':
    main()
    
