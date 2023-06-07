class SimsSimulation:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def log_events(self):
        for event in self.events:
            print(event)

# Створюємо об'єкт симуляції
simulation = SimsSimulation()

# Додавання подій до симуляції
simulation.add_event("Симуляція розпочалася")
simulation.add_event("Симуляція в процесі")
simulation.add_event("Симуляція завершена")

# Логування подій
simulation.log_events()