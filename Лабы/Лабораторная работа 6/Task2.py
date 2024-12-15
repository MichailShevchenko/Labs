class Vehicle:
    make = None
    model = None
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        print(f"Марка: {self.make}, модель: {self.model}")

class car(Vehicle):
    def __init__(self, fuel_type, make, model):
        super(car, self).__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        print(f"Марка: {self.make}, модель: {self.model}, тип топлива: {self.fuel_type}")

Vehicle1 = Vehicle("Икарус", "256")
car1 = car("АИ-95", "Toyota", "Supra")
Vehicle1.get_info()
car1.get_info()