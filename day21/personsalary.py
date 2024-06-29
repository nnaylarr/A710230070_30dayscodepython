class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

oPerson1 = Person('shawn', 90000)
oPerson2 = Person('nopal', 99000)

print(oPerson1.salary)
print(oPerson2.salary)

oPerson1.salary = 100000
oPerson2.salary = 111111

print(oPerson1.salary)
print(oPerson2.salary)
