import operator
import random


class People:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


names = ["Дмитрий", "Александр", "Алексей", "Сергей", "Екатерина", "Пётр", "Анастасия"]
mass = []
for i in range(15):
    people = People(random.choice(names), random.randrange(10, 80, 1), random.randrange(30, 150, 1))
    mass.append(people)

sort_age = sorted(mass, key=operator.attrgetter('age'))
sort_weight = sorted(mass, key=operator.attrgetter('weight'))

with open("1\\result_sort_age", "w", encoding="utf-8") as file:
    for people in sort_age:
        file.write(f'{people.name} {people.age} {people.weight} \n')

with open("1\\result_sort_weight", "w", encoding="utf-8") as file:
    for people in sort_weight:
        file.write(f'{people.name} {people.age} {people.weight} \n')
