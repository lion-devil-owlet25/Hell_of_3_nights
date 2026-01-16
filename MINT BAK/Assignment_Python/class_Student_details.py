class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name, " Roll:", self.roll, " Marks:", self.marks)


s1 = Student("Rahul", 101, 85)
s2 = Student("Sumi", 102, 90)

s1.display()
s2.display()
