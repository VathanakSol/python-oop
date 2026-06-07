# Abstraction 
# abc = abstract based class
# import module
from abc import ABC, abstractmethod

# abstract class
class Person(ABC):

    @abstractmethod
    def show_info(self):
        pass

class Student(Person):

    # method overriding
    # implement abstract method
    def show_info(self):
        print("This is show info abstract")

    def display(self):
        print("This is student")

# stu = Student()
# stu.display()

class Exam(ABC):

    @abstractmethod
    def __init__(self, teacher, location):
        pass

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def card(self):
        pass

class History(Exam):
    def __init__(self, teacher, location):
        self.__teacher = teacher
        self.__location = location
    
    @property
    def get_teacher(self):
        return self.__teacher
    
    @property
    def get_location(self):
        return self.__location

    def security(self):
        print(f"This is security for watchout candidate. check by {self.get_teacher}")

    def card(self):
        print(f"Candicate must have card to allow exam. At {self.get_location}")

his1 = History("teacher A", "PP")
his2 = History("teacher B", "SR")

his2.card()