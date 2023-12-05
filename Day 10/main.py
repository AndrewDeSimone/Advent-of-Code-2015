import re
data = open('Day 10\\input.txt', 'r').read()

def lookSay(n):
    new = ''
    current = ''
    count = 0
    for i in n:
        if current == '':
            current = i
            count += 1
        elif current == i:
            count+=1
        else:
            new += str(count) + current
            current = i
            count = 1
    new += str(count) + current
    return new 

for i in range(0, 50):
    data = lookSay(data)
print(len(data))