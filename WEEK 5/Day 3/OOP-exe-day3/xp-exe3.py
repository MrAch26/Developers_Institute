from random import randint

def get_num():
    number = randint(1,10)
    return number

def pwr(func):
    number = func()
    print(number, number*number)

pwr(get_num) # 1 1