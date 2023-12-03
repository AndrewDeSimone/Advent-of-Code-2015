import re

input = open('Day 7\\input.txt', 'r').read().split('\n')

wires = {}

for i in input:
    instruction = i.split(' -> ')
    wires[instruction[1]] = instruction[0]

def evaluate(wire):
    if isinstance(wires[wire], int):
        return wires[wire]
    instruction = wires[wire].split(' ')
    if len(instruction) == 1:
        if re.sub('[^0-9]', '', instruction[0]):
            return wires[wire]
        else:
            wires[wire] = evaluate(instruction[0])
            return wires[wire]
    if len(instruction) == 2:
        wires[wire] = int(evaluate(instruction[1])) ^ 0xffff
        return wires[wire]
    if instruction[1] == 'LSHIFT':
        wires[wire] = int(evaluate(instruction[0])) << int(instruction[2])
        return wires[wire]
    if instruction[1] == 'RSHIFT':
        wires[wire] = int(evaluate(instruction[0])) >> int(instruction[2])
        return wires[wire]
    if instruction[1] == 'AND':
        if re.sub('[^0-9]', '', instruction[0]):
            wires[wire] = int(instruction[0]) & int(evaluate(instruction[2]))
        else:
            wires[wire] = int(evaluate(instruction[0])) & int(evaluate(instruction[2]))
        return wires[wire]
    if instruction[1] == 'OR':
        wires[wire] = int(evaluate(instruction[0])) | int(evaluate(instruction[2]))
        return wires[wire]
    
    

print('a:',evaluate('a'))