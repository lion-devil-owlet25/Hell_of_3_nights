class Animal:
    def sound(self):
        print("Animal sound")

class Bird(Animal):
    def sound(self):
        print("Bird sound")

class Mammal(Animal):
    def sound(self):
        print("Mammal sound")

# Diamond problem
class Bat(Bird, Mammal):
    pass

b = Bat()
b.sound()   # Follows MRO

