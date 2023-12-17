import re
data = open('Day 16\\input.txt', 'r').read().split('\n')

rules = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for i in data:
    number = int(re.sub('[^0-9]', '', i.split(':')[0]))
    i = re.sub(' ','',''.join(i.split(':')[1:]))
    possible = True
    possible2 = True
    for j in i.split(','):
        thing = re.sub('[0-9]', '', j)
        count = int(re.sub('[^0-9]', '', j))
        if count != rules[thing]:
            possible = False
        if thing in ['cats', 'trees']:
            if count <= rules[thing]:
                possible2 = False
        elif thing in ['pomeranians', 'goldfish']:
            if count >= rules[thing]:
                possible2 = False
        else:
            if count != rules[thing]:
                possible2 = False
    if possible:
        print(f'Part 1: {number}')
    if possible2:
        print(f'Part 2: {number}')
