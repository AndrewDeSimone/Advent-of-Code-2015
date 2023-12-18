import numpy as np 

testedRange = 1000000

houses = np.array([0 for i in range(0, testedRange)])

for i in range(1, testedRange):
    starting = i
    while i < len(houses):
        houses[i] += starting * 10
        i+=starting

for i in range(0, len(houses)):
    if houses[i] >= 29000000:
        print(f'Part 1: {i}')
        break

houses = np.array([0 for i in range(0, testedRange)])
for i in range(1, testedRange):
    count = 0
    starting = i
    while i < len(houses) and count < 50:
        houses[i] += starting * 11
        count += 1
        i+=starting

for i in range(0, len(houses)):
    if houses[i] >= 29000000:
        print(f'Part 2: {i}')
        break