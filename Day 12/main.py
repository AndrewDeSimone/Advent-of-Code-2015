import re
import json
data = open('Day 12\\input.txt', 'r').read()
temp = re.findall('-?[0-9]+', data)

sum = 0

for i in temp:
    sum += int(i)

print(f'Part 1: {sum}')

data = json.loads(data)

def sum(object):
    if type(object) == type(dict()):
        if "red" in object.values():
            return 0
        parts = 0
        for i in object.values():
            parts += sum(i)
        return parts
    if type(object) == type(list()):
        parts = 0
        for i in object:
            parts += sum(i)
        return parts
    if type(object) == type(0):
        return object

    return 0

print(f'Part 2: {sum(data)}')