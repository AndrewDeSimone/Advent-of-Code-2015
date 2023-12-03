input = open('Day 3\\input.txt', 'r').read()

x = [0, 0]
y = [0, 0]

turn = 0

visited = {(0,0)}

for i in input:
    if i == '>':
        x[turn] += 1
    if i == '<':
        x[turn] -= 1
    if i == '^':
        y[turn] -= 1
    if i == 'v':
        y[turn] += 1
    visited.add((x[turn],y[turn]))
    turn = turn ^ 1

print(len(visited))