import re

data = open('Day 11\\input.txt', 'r').read()

def containsStraight(string):
    for i in range(2, len(string)):
        if ord(string[i]) - 1 == ord(string[i-1]) and ord(string[i-1]) - 1 == ord(string[i-2]):
            return True
    return False

def containsLegalCharacters(string):
    if re.search('i|o|l', string):
        return False
    return True

def containsDoubleLetters(string):
    return len(re.findall(r'(.)\1', string)) > 1

def legalPassword(password):
    return containsDoubleLetters(password) and containsLegalCharacters(password) and containsStraight(password)

def incrementString(string):
    string = list(string)
    holder = string.pop()
    if holder == 'z':
        string = incrementString(string)+'a'
    else:
        string.append(chr(ord(holder)+1))
    return ''.join(string)

while not legalPassword(data):
    data = incrementString(data)

print(f'Part 1: {data}')

data = incrementString(data)
while not legalPassword(data):
    data = incrementString(data)

print(f'Part 2: {data}')