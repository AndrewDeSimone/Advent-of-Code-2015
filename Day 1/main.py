input = open('Day 1\\input.txt', 'r').read()
floor = 0
count = 0
basemented = False

for i in input:
    if i == '(':
        floor += 1
    else:
        floor -= 1
    count += 1
    if not basemented and floor == -1:
        basemented = True
        print(f'Basement {count}')

print(floor)