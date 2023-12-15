import re
data = open('Day 14\\input.txt', 'r').read().split('\n')

farthest = 0
distanceboard = []


for reindeer in data:
    distanceboard.append([])
    speed, time, rest = map(int, re.findall(r'[0-9]+', reindeer))
    distance = 0
    seconds = 0
    while seconds < 2503:
        if seconds % (time+rest) < time:
            distance+=speed
        seconds += 1
        distanceboard[len(distanceboard)-1].append(distance)
    farthest = max(farthest, distance)

print(f'Part 1: {farthest}')

totals = [0 for i in distanceboard]

for i in range(0, len(distanceboard[0])):
    current = []
    for j in range(len(distanceboard)):
        current.append(distanceboard[j][i])
    most = max(current)
    for i in range(0,len(current)):
        if current[i] == most:
            totals[i]+=1


print(f'Part 2: {max(totals)}')