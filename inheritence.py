class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def hello(self):
        print( f"Hello {self.first_name} {self.last_name}, age {self.age}!")

class Employee(Person):
    def say_hello(self):
        print("----")
        super().hello()
        print("----")

e= Employee("John", "Doe", 28)
print(e.say_hello())

