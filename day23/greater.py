class Greeter:
    def __init__(self, greeter):
        self.greeter = greeter

    def greet(self):
        return self.greeter.greet()

class EnglishGreeter:
    def greet(self):
        return 'Hello!'

class SpanishGreeter:
    def greet(self):
        return '¡Hola!'

class FrenchGreeter:
    def greet(self):
        return 'Bonjour!'

english_greeter = EnglishGreeter()
spanish_greeter = SpanishGreeter()
french_greeter = FrenchGreeter()
greeter = Greeter(english_greeter)
print(greeter.greet()) 

greeter = Greeter(spanish_greeter)
print(greeter.greet()) 

greeter = Greeter(french_greeter)
print(greeter.greet()) 
