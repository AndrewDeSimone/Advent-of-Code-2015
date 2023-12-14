from itertools import permutations
import sys
data = open('Day 13\\input.txt', 'r').read().split('\n')

people = set()
relations = {}

for rule in data:
    rule = rule.split(' ')
    people.add(rule[0])
    partners = (rule[0], rule[-1][:-1])
    gain = int(rule[3])
    if rule[2] == 'lose':
        gain *= -1
    relations[partners] = gain

maxHappy = -10000000
for i in list(permutations(people)):
    happiness = 0
    for j in range(0, len(i)):
        happiness += relations[(i[j], i[j-1])]
        if j != len(i)-1:
            happiness += relations[(i[j], i[j+1])]
        else:
            happiness += relations[(i[j], i[0])]
    maxHappy = max(maxHappy, happiness)

print(f'Part 1: {maxHappy}')

for i in people:
    relations[(i, 'me')] = 0
    relations[('me', i)] = 0

people.add('me')

maxHappy = -10000000
for i in list(permutations(people)):
    happiness = 0
    for j in range(0, len(i)):
        happiness += relations[(i[j], i[j-1])]
        if j != len(i)-1:
            happiness += relations[(i[j], i[j+1])]
        else:
            happiness += relations[(i[j], i[0])]
    maxHappy = max(maxHappy, happiness)

print(f'Part 2: {maxHappy}')