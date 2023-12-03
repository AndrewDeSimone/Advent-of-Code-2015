import hashlib

input = open('Day 4\\input.txt', 'r').read()

count = 0
while True:
    temp = input + str(count)
    if hashlib.md5(temp.encode()).hexdigest()[0:6] == '000000':
        print(count)
        quit()
    count += 1
