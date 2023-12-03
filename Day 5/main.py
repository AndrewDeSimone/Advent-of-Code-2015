import re

input = open('Day 5\\input.txt', 'r').read().split('\n')

count = 0

for i in input:
    #3 vowels
    if len(re.findall('[aeiou]', i)) >= 3:
        #repeating letters
        if len(re.findall('(.)\\1', i)) >= 1:
            #exclude letters
            if len(re.findall('ab|cd|pq|xy', i)) == 0:
                count += 1

print('Old Nice:', count)

count = 0

for i in input:
    if (len(re.findall('(.).\\1', i))) >= 1:
        if (len(re.findall('(.)(.).*\\1\\2', i))) >= 1:
            count += 1

print('New Nice:', count)
