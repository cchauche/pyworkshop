# chapter_6.py

class Car:
    runs = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        if self.runs:
            print(f"My {self.make} {self.model} started. Vroom vroom!")
        else:
            print(f"My {self.make} {self.model}  is broken :(")


my_car = Car("Toyota", "Corolla")
print(f"My car runs: {my_car.runs}")
my_car.start()
my_car.runs = False
my_car.start()
