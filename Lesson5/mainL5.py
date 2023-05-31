'''
import requests as requests
from requests import get
from requests import post

help(requests)

r = requests.get('https://www.python.org')
print(r.status_code)
print(r.content)

payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''
import colorama as colorama

'''
from studentL5 import Student
studentL5 = Student()
print(Student.__name__)
print(Student.__bases__)
print(type(Student))
'''

students = list()
for method in dir (students):
    print(method)

help(list)
from studentL5 import Student, Pupil
print(issubclass(Student, Pupil))
'''
getattr()
callable()
insubclass()
isinstance()
'''

help(colorama)