import re

input = open('Day 2\\input.txt').read()

boxes = re.findall('\d+x\d+x\d+', input)

wrappingPaper = 0
ribbon = 0

for box in boxes:
    dimensions = [int(i) for  i in re.findall('\d+', box)]
    areas = [dimensions[0]*dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]]
    wrappingPaper += 2 * (areas[0] + areas[1] + areas[2]) + min(areas)
    ribbon += dimensions[0] * dimensions[1] * dimensions[2] + sorted(dimensions)[0] * 2 + sorted(dimensions)[1] * 2
print("WrappingPaper:", wrappingPaper)
print("Ribbons:", ribbon)
