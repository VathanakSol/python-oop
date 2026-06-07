# Polymorphism = many form 
# Parent Class 
class Animal:
    def make_sound(self):
        print("Animal make sound")

# Subclass / Child class
class Cow(Animal):
    def make_sound(self):
        print("Mohrrrr")

class Cat(Animal):
    def make_sound(self):
        print("Meowww")

class Dog(Animal):
    pass

# cow = Cow()
# cow.make_sound()
# cat = Cat()
# cat.make_sound()
# dog = Dog()
# dog.make_sound()

class Payment:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def get_balance(self):
        return self.__balance

class VisaCard(Payment):
    def pay(self):
        print(f"You have purchase via visacard {self.get_balance}")

class MasterCard(Payment):
    def pay(self):
        print(f"You have purchase via mastercard {self.get_balance}")

class BakongQR(Payment):
    def pay(self):
        print(f"You have purchase via bakongQR {self.get_balance}")        

payment_method = [VisaCard(200), MasterCard(500), BakongQR(1000)]

for payment in payment_method:
    payment.pay()


# def checkout(payment_method, balance):
#     payment_method(balance).pay()

# checkout(VisaCard, 500)
# checkout(MasterCard, 200)
# checkout(BakongQR, 700)

# pay1 = VisaCard(2000)
# pay2 = MasterCard(3000)

# pay1.pay() 
# pay2.pay()       

