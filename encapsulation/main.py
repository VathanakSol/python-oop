# Encapsulation 

class Person:
    def __init__(self, name, age, job):
        # Public 
        self.name = name
        self.age = age

        # Protected
        self._job = job

        # Privated 
        self.__id = "abc123"

    def show_name(self):
        pass

# p1 = Person("kaka", 18, "student")
# mangling name 
# print(p1._Person__id) 

class BankAccount:
    def __init__(self, acc_name, deposit):
        # public
        self.acc_name = acc_name
        # protected
        self._deposit = deposit
        # private
        self.__balance = 2000

    def check_balance(self):
        print(f"Total balance is: {self.__balance}")

    def deposit_balance(self):
        total = self.__balance + self._deposit
        print(f"Total balance is {total}") 

bank = BankAccount("myacc",-500)
# bank.check_balance()
# bank.deposit_balance()

# Getter and Setter 
# decorator @

class School:
    def __init__(self, name, address, year, school_id, revenue):
        self.name = name
        self.address = address
        self._year = year
        self.__school_id = school_id
        self.__revenue = revenue

    @property
    def revenue(self):
        return self.__revenue

    # Getter
    @property
    def year(self):
        return self._year
    
    # Getter
    @property
    def school_id(self):
        return self.__school_id

s1 = School("myschool", "pp", 5, "xyz123", 20000)

# print(s1.name)
# print(s1.address)
# print(s1.year)
# print(s1.school_id)
# print(s1.revenue)


