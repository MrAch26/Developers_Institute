class Test:
    def __init__(self, age):
        self.name = 'daniel'
        self.age = age
    def sababa(self):
        print (f'{self.name} {self.age} hahaha')


def main():
    test = Test(26)
    print(test.name)
    test.sababa()

if __name__ == '__main__':
    main()