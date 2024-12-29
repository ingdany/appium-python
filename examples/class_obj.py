class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show(self):
        print(f"{self.make} and {self.model}")


honda = Car("Honda", "City")
honda.show()


Maruti = Car("Swift", "X")
Maruti.show()


# Inheritance
class VW(Car):
    def __init__(self, make, model, color, year):
        super().__init__(make, model)
        self.color = color
        self.year = year

    def show(self):
        print(f"{self.make}, {self.model}, {self.color}, {self.year}")


vw1 = VW("polo", "GT", "red", "2022")
vw1.show()


# encapsulation
class Bank:
    def __init__(self, account):
        self.__account = account  # private

    def get_account(self):
        return self.__account


bank = Bank(1232)
print(bank.get_account())
