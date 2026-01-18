class Complex:
    count = 0
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        Complex.count += 1
    def display(self):
        print(f"{self.real} + {self.imag}i")
c1 = Complex(3, 4)
c2 = Complex(5, 6)
c3 = Complex(1, -2)
c1.display()
c2.display()
c3.display()
print("Total Complex Numbers Created =", Complex.count)

