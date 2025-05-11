import math
import time
from datetime import datetime

class MobilePhone:

    def __init__(self, brand, model, color, battery):
        print('new phone created')
        self.brand = brand
        self.model = model
        self.color = color
        self.battery = battery
        self.created_at = datetime.now()

    def __str__(self) -> str:
        # print(self.__dict__)
        return f"mobile_phone.MobilePhone brand=[{self.brand}] model=[{self.model}] " + \
               f"color=[{self.color}] battery=[{self.color}] created_at=[{self.created_at}]" +\
               f"datetime={datetime.now().__str__()}"

    # 1. str-like
    # 2. developer-code
    def __repr__(self):
        # 1. str-like
        # worse
        # return f"mobile_phone.MobilePhone brand=[{self.brand}] model=[{self.model}] " + \
        #        f"color=[{self.color}] battery=[{self.color}] created_at=[{self.created_at}]" +\
        #        f"datetime={datetime.now().__str__()}"
        # better
        # return self.__str__()

        # 2. developer-mode i.e. save time for next time
        #    MobilePhone('Samsung', 'S25Ultra', 'black', 25)
        return f"MobilePhone('{self.brand}', '{self.model}', '{self.color}', {self.battery})"

    def __del__(self):
        print(f"MobilePhone {self.model} {self.brand} is being removed!")

def add(x: int, y: int) -> int:
    x = x
    return x + y

# בנאי
# constructor
# init
samsung = MobilePhone('Samsung', 'S25Ultra', 'black', 25)
iphone = MobilePhone('IPhone', '16pro', 'white', 79)

# new1 = MobilePhone(samsung.brand, ...)

# new2 = MobilePhone('Samsung', 'S25Ultra', 'black', 25)

# db = DbConn(...)  # long
# repr_db = db.__repr__()
# db.connect

# eval playground
# eval("print('hello, running via eval')")
#
# command = input('enter command:')
# while command != 'exit':
#     eval(command)
#     command = input('enter command:')



bag: list[MobilePhone] = [samsung, iphone]
print(bag)  # __repr__ : 1. inside container 2. developer-code
print({'phone': samsung})
print(samsung.__repr__())

print(samsung.__dict__)

d = dict()
d['id'] = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
       return f"x = {self.x} y = {self.y} distance = {math.sqrt(self.x ** 2 + self.y ** 2)}"

p1 = Point(5.7, 9.9)
p2 = Point(5.9, 10.9)

p1.x = p1.x ** 2
# samsung.brand = "Samsung"
# samsung.model = "S25Ultra"
# samsung.color = "Black"
# samsung.battery = 25

samsung.screen_protector = 'glass'
del samsung.screen_protector

# create UML for class Person
# id: int
# name: str
# height: float
# salary: int
# init -- with all parameters
# write a class Person + create instance with some data

print(samsung)  # __str__ ( )

def a():
    n = MobilePhone('Samsung!!', 'S25Ultra', 'black', 25)
    time.sleep(1)

a()
time.sleep(1)
print('bye')
# override
# <module.Class-name object at HashCode [0x000001D3D3723EE0]>



