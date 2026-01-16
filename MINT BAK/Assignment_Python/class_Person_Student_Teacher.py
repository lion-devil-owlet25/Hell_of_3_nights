class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks
    def display(self):
        super().display()
        print(f"Roll: {self.roll}, Marks: {self.marks}")

class Teacher(Person):
    def __init__(self, name, age, subject, exp):
        super().__init__(name, age)
        self.subject = subject
        self.exp = exp
    def display(self):
        super().display()
        print(f"Subject: {self.subject}, Experience: {self.exp} years")

s = Student("Anita", 20, 101, 88.5)
t = Teacher("Mr. Das", 40, "Maths", 15)
print("----Student Record---")
s.display()
print("----Teachers Record---")
t.display()

