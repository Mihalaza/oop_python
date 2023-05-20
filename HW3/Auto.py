class Human:
    def init(self, name=None):
        self.name = name

class Auto:
    def init(self, brand=None):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()

    def AddPassenger(self, human):
        self.Passengers.append(human)

    def AddDriver(self, human):
        self.Drivers.append(human)

    def ToStringDriver(self, driverName):
        print(f"Driver of {self.Brand} is {driverName}")

    def ToStringPassenger(self, passengerName):
        print(f"Passenger of {self.Brand} is {passengerName}")


# Створюємо об'єкти людини
john = Human("John")
emma = Human("Emma")

# Створюємо об'єкт автомобіля
car = Auto("Toyota")

# Додаємо водія та пасажирів до автомобіля
car.AddDriver(john)
car.AddPassenger(emma)

# Викликаємо методи для виведення інформації про водія та пасажира
car.ToStringDriver(john.name)
car.ToStringPassenger(emma.name)
