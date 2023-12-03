import re

input = open('Day 6\\input.txt', 'r').read().split('\n')

grid = [[0 for i in range(1000)] for i in range(1000)]

for i in input:
    instruction = re.sub('turn |through ', '', i).split(' ')
    for i in range(int(instruction[1].split(',')[0]), int(instruction[2].split(',')[0])+1):
        for j in range(int(instruction[1].split(',')[1]), int(instruction[2].split(',')[1])+1):
            if instruction[0] == 'on':
                grid[i][j] += 1
            if instruction[0] == 'off':
                if grid[i][j] != 0:
                    grid[i][j] -= 1
            if instruction[0] == 'toggle':
                grid[i][j] += 2

sum = 0

for i in range(0, len(grid)):
    for j in range(0,len(grid[0])):
        sum += grid[i][j]

print(sum)