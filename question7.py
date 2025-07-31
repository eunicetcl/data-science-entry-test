class Car:
    """
    This class represents a car with make, model, and year.
    It has a method to describe the car in the format: "Year Make Model".
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Example
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()
