from human import Human
from human import Speak
class InStepStudent(Human, Speak):
    def __init__(self, group, avgGrade):
        super().__init__(name, age, height)
        self.Group = group
        self.AvgGrade = avgGrade
        self.SayName(name)
    def __str__(self):
        return f"{super().__str__()}Group: {self.Group}\nAvg grade: {self.AvgGrade}"