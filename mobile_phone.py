import datetime


class MobilePhone:

    def __init__(self, brand, model, color, battery):
        print('new phone created')
        self.brand = brand
        self.model = model
        self.color = color
        self.battery = battery
        self.created_at = datetime.now()

def add(x: int, y: int) -> int:
    x = x
    return x + y

# בנאי
# constructor
# init
samsung = MobilePhone('Samsung', 'S25Ultra', 'black', 25)
iphone = MobilePhone('IPhone', '16pro', 'white', 79)

d = dict()
d['id'] = 1

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

