from itertools import combinations_with_replacement
data = open('Day 15\\input.txt', 'r').read().split('\n')

ingredients = {}

for i in data:
    name = i.split(':')[0]
    ingredients[name] = {
        'capacity': int(i.split(' ')[2][:-1]),
        'durability': int(i.split(' ')[4][:-1]),
        'flavor': int(i.split(' ')[6][:-1]),
        'texture': int(i.split(' ')[8][:-1]),
        'calories': int(i.split(' ')[10])
    }

bestCookie = None
bestCookieWithCals = None

for i in list(combinations_with_replacement(ingredients.keys(), 100)):
    current = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
        'calories': 0
    }
    for j in i:
        current['capacity'] += ingredients[j]['capacity']
        current['durability'] += ingredients[j]['durability']
        current['flavor'] += ingredients[j]['flavor']
        current['texture'] += ingredients[j]['texture']
        current['calories'] += ingredients[j]['calories']
    for j in current.keys():
        if current[j] < 0:
            current[j] = 0
    calories = current['calories']
    current = current['capacity'] * current['durability'] * current['flavor'] * current['texture']
    if bestCookie:
        bestCookie = max(current, bestCookie)
    else:
        bestCookie = current
    if calories == 500:
        if bestCookieWithCals:
            bestCookieWithCals = max(current, bestCookieWithCals)
        else:
            bestCookieWithCals = current


print(f'Part 1: {bestCookie}')
print(f'Part 2: {bestCookieWithCals}')