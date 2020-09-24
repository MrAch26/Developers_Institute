# EXE1
class Family():
    def __init__(self, last_name,members=[]):
        self.members = members
        self.last_name = last_name

    def born(self, **memberinfo):
        self.members.append(memberinfo)
    
    def is_child_18(self, name):
        for i in range(len(self.members)):
            if self.members[i]['name'] == name:
                if self.members[i]['age'] >= 18:
                    return True
                else:
                    return False
    
    def __repr__(self):
        output = [self.last_name]
        for member in self.members:
            output.append(f"name: {member['name']}, age: {member['age']}, gender: {member['gender']}")
        return "\n".join(output)

members1 = [{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}]
def main():
    ach = Family("Ach's Family",members1)
    ach.born(name='Daniel', age = 22, gender = 'male')
    print(ach.members)
    # print(ach.is_child_18('Daniel'))
    print(repr(ach))

if __name__ == '__main__':
    main()
    