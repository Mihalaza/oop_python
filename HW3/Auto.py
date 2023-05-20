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
miha = Human("Miha")
katya = Human("Katya")

# Створюємо об'єкт автомобіля
car = Auto("Toyota")

# Додаємо водія та пасажирів до автомобіля
car.AddDriver(miha)
car.AddPassenger(katya)

# Викликаємо методи для виведення інформації про водія та пасажира
car.ToStringDriver(miha.name)
car.ToStringPassenger(katya.name)
