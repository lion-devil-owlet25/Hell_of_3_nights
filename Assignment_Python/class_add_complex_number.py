class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real}{sign}{abs(self.imag)}i"

    def add(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

# Test
c1 = Complex(3, 4)
c2 = Complex(1, -2)

print("First:", c1)
print("Second:", c2)
print("Sum:", c1.add(c2))

