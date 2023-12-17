data = open('Day 17\\input.txt', 'r').read().split('\n')

containers = [int(i) for i in data]
mappedContainers = {}
minimumContainers = -1

total = 0

for i in range(0, 2**len(containers)):
    temp = bin(i)
    temp = list(map(int, temp.split('b')[1]))
    while len(temp) != len(containers):
        temp.insert(0,0)
    count = 0
    amountOfContainers = 0
    for j in range(0,len(temp)):
        if temp[j] == 1:
            amountOfContainers += 1
        count += temp[j] * containers[j]
    if count == 150:
        if minimumContainers == -1:
            minimumContainers = amountOfContainers
        else:
            minimumContainers = min(amountOfContainers, minimumContainers)
        if amountOfContainers in mappedContainers.keys():
            mappedContainers[amountOfContainers] += 1
        else:
            mappedContainers[amountOfContainers] = 1
        total += 1

print(f'Part 1: {total}')
print(f'Part 2: {mappedContainers[minimumContainers]}')