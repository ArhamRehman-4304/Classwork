class Cars:
    def __init__(self, make, model, year, drivetrain):
        self.make = make
        self.model = model
        self.year = year
        self.drivetrain = drivetrain

    def car_info(self):
            return f"The {self.model} is a {self.year}, made by {self.make} and has a {self.drivetrain} drivetrain."
        
    def is_all_wheel_drivetrain(self):
        return self.drivetrain == "AWD"
        
#creating objects (instances)
car1 = Cars("Toyota", "Camry", 2020, "FWD")
car2 = Cars("Subaru", "Outback" , 2021, "AWD")

print(car1.car_info())
print(car2.car_info())

