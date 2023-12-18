import re
swaps, start = open('Day 19\\input.txt', 'r').read().split('\n\n')
swaps = swaps.split('\n')

molecules = set()

for i in swaps:
    initial, changes = i.split(' => ')
    for j in range((len(start) - len(initial))+1):
        if start[j:j+len(initial)] == initial:
            molecules.add(start[:j]+changes+start[j+len(initial):])

print(f'Part 1: {len(molecules)}')

count = 0

start = re.sub('Rn', '(', start)
start = re.sub('Ar', ')', start)
start = re.sub('Y', ',', start)
start = re.sub('[a-z]', '', start)
openCount = len(re.findall(r"\(", start))
closeCount = len(re.findall(r"\)", start))

print(f'Part 2: {len(start) - openCount - closeCount - 2*len(re.findall(",", start)) - 1}')