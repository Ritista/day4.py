# function

def a(name, age):
    print(f"hello {name}")
    print(f"age {age}")
a("ritista", 23)
a("sachita", 23)

def b(name, age = 10):
    print(f"hello {name}")
    print(f"age {age}")
b("ritista")
b("sachita", 23)

class Main:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{name} and {age}")


    def __str__(self):
        print(f"{self.name} and age {self.age} from main class con in method{main}")
class Hello(Main):
    def __init__(self, name, age, location):
        super().__init__(name, age)
        self.location = location
        print(f"{name} and {age} and {location}")
c = Hello("riti", 23, "ktm")


import datetime
e = datetime.datetime.now()
print(e)

i = datetime.datetime.today()
print(i)

i = datetime.datetime.now().year
print(i)

i = datetime.datetime.today().day
print(i)
# scope
# global variable

f = 10
def g():
    h = 20
    print(h)
    print(f)
g()
print(f)
