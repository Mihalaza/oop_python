'''from counter import Counter

name = "Miha"
#for a in iter(name):#range
    #print(a)

try:
    iterator = iter(name)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print()

#Counter
counter = Counter(9)
for i in counter:
    print(i)
'''
from generator import Generator
generator = Generator(0)
res = generator.Raise_to_the_degrees_F(122345,500)
print(res)
for item in generator.Raise_to_the_degrees_F(122345, 500):
    print(f"{item}\n")