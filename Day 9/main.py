import itertools

data = open('Day 9\\input.txt', 'r').read().split('\n')

cities = set()
distances = {}

for i in data:
    temp = i.split()
    cities.add(temp[0])
    cities.add(temp[2])
    distances[temp[0]+temp[2]] = int(temp[4])

cities = list(cities)
cityLists = list(itertools.permutations(cities))

maximum = 'none'
minimum = 'none'

for sequence in cityLists:
    distance = 0
    for i in range(0,len(sequence)-1):
        if sequence[i]+sequence[i+1] in distances.keys():
            distance += distances[sequence[i]+sequence[i+1]]
        else:
            distance += distances[sequence[i+1]+sequence[i]]
    if minimum == 'none':
        minimum = distance
    else:
        minimum = min(minimum, distance)
    if maximum == 'none':
        maximum = distance
    else:
        maximum = max(maximum, distance)

print(minimum)
print(maximum)
