import mod
import math  # inbuild


def greeting():
    print("Hello Everyone")


greeting()


# parameter functions
def add(a, b):
    add1 = a + b
    print(add1)


add(5, 7)
add(5, 10)


# return functions
def multi(a, b):
    return a * b


value = multi(5, 3)
print(value)


# default value function paramater
def username(name="Not a Name"):
    print(name)


username()


mod.show()


def div(a):
    print(math.sqrt(a))


div(4)
