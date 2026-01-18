class Car:
    count = 0

    def __init__(self, car_id, car_name):
        self.car_id = car_id
        self.car_name = car_name
        Car.count += 1

    def display(self):
        print("Car ID:", self.car_id, " Car Name:", self.car_name)
car1 = Car(1, "BMW")
car2 = Car(2, "Audi")
car1.display()
car2.display()
print("Total Cars Created =", Car.count)
