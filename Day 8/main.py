import re
data = open('Day 8\\input.txt', 'r').read().split('\n')

sumLit = 0
sumMem = 0
sumEncode = 0

for i in data:
    sumLit += len(i)
    temp = i
    temp = temp[1:len(temp)-1]
    temp = re.sub(r'\\"', 'a', temp)
    temp = re.sub(r'\\\\', 'a', temp)
    temp = re.sub(r'\\x..', 'a', temp)
    sumMem += len(temp)

    encoded = i
    encoded = re.sub(r'\"', '123', encoded)
    encoded = re.sub(r'\\"', '1234', encoded)
    encoded = re.sub(r'\\\\', '1234', encoded)
    encoded = re.sub(r'\\x..', '12345', encoded)
    sumEncode += len(encoded)



print(sumLit-sumMem)
print(sumEncode-sumLit)

