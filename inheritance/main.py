# Inheritance 
class A:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def show_info(self):
        print("This is class A")

class B(A):
    pass

class C(A):
    pass

c = C(10,20)
print(c.num1, c.num2)

# Type of Inheritance
# -------------------
# Single Inheritance

class Animal:
    def sleep(self):
        print("This is sleep")
    def walk(self):
        print("This is walk")
    def sound(self):
        print("This is sound")

class Dog(Animal):
    def name(self):
        print("Dog name is ...")

dog = Dog()
# dog.name()
# dog.sleep()
# dog.walk()
# dog.sound()

# Multiline Inheritance
class A:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def show_info(self):
        print("This is class A")

class B(A):
    def show_result(self):
        print(f"{self.num1 + self.num2}")

class C(B):
    pass

c = C(20,30)
c.show_result()

# Multi-level Inheritance
class A:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def show_info(self):
        print("This is class A")

class B:
    def get_info(self):
        print("This is from Class B")

class C(A, B):
    pass

class D(C):
    pass

d = D(25,75)
d.get_info()

# Hybrid : Combine like multiline or multilevel in one place