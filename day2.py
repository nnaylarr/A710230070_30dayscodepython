class Duck:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Wek Wek")  

class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Bark Bark")

class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Meoooww")

my_duck = Duck("Bebek")
my_duck.sound()  

my_dog = Dog("Anjing")
my_dog.sound()  

my_cat = Cat("Kucing")
my_cat.sound()  
