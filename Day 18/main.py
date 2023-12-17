data = open('Day 18\\input.txt', 'r').read().split('\n')
grid = [list(i) for i in data]
grid2 = grid.copy()
grid2 = [i.copy() for i in grid2]

grid2[0][0] = '#'
grid2[len(grid2)-1][0] = '#'
grid2[0][len(grid2[0])-1] = '#'
grid2[len(grid2)-1][len(grid2[0])-1] = '#'

def getNextGrid(grid):
    newGrid = grid.copy()
    newGrid = [i.copy() for i in newGrid]
    for i in range(0,len(grid)):
        for j in range(0, len(grid[0])):
            neighbors = 0
            if i > 0:
                if grid[i-1][j] == '#':
                    neighbors+=1
                if j > 0:
                    if grid[i-1][j-1] == '#':
                        neighbors+=1
                if j < len(grid[0])-1:
                    if grid[i-1][j+1] == '#':
                        neighbors+=1
            if i < len(grid)-1:
                if grid[i+1][j] == '#':
                    neighbors+=1
                if j > 0:
                    if grid[i+1][j-1] == '#':
                        neighbors+=1
                if j < len(grid[0])-1:
                    if grid[i+1][j+1] == '#':
                        neighbors+=1
            if j > 0:
                if grid[i][j-1] == '#':
                        neighbors+=1
            if j < len(grid[0])-1:
                    if grid[i][j+1] == '#':
                        neighbors+=1
            if grid[i][j] == '#':
                if neighbors in [2,3]:
                    newGrid[i][j] = '#'
                else:
                    newGrid[i][j] = '.'
            else:
                if neighbors == 3:
                    newGrid[i][j] = '#'
                else:
                    newGrid[i][j] = '.'

    return newGrid

def getNextGridBrokenLight(grid):
    newGrid = grid.copy()
    newGrid = [i.copy() for i in newGrid]
    for i in range(0,len(grid)):
        for j in range(0, len(grid[0])):
            neighbors = 0
            if i > 0:
                if grid[i-1][j] == '#':
                    neighbors+=1
                if j > 0:
                    if grid[i-1][j-1] == '#':
                        neighbors+=1
                if j < len(grid[0])-1:
                    if grid[i-1][j+1] == '#':
                        neighbors+=1
            if i < len(grid)-1:
                if grid[i+1][j] == '#':
                    neighbors+=1
                if j > 0:
                    if grid[i+1][j-1] == '#':
                        neighbors+=1
                if j < len(grid[0])-1:
                    if grid[i+1][j+1] == '#':
                        neighbors+=1
            if j > 0:
                if grid[i][j-1] == '#':
                        neighbors+=1
            if j < len(grid[0])-1:
                    if grid[i][j+1] == '#':
                        neighbors+=1
            if grid[i][j] == '#':
                if neighbors in [2,3]:
                    newGrid[i][j] = '#'
                else:
                    newGrid[i][j] = '.'
            else:
                if neighbors == 3:
                    newGrid[i][j] = '#'
                else:
                    newGrid[i][j] = '.'
    newGrid[0][0] = '#'
    newGrid[len(newGrid)-1][0] = '#'
    newGrid[0][len(newGrid[0])-1] = '#'
    newGrid[len(newGrid)-1][len(newGrid[0])-1] = '#'

    return newGrid


for i in range(0, 100):
    grid = getNextGrid(grid)
    grid2 = getNextGridBrokenLight(grid2)

count = 0
count2 = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == '#':
            count+=1
        if grid2[i][j] == '#':
            count2+=1

print(f'Part 1: {count}')
print(f'Part 2: {count2}')