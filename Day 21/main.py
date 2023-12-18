import re
import math

def formatStoreItems(category):
    category = category.split('\n')[1:]
    for i in range(0, len(category)):
        item = category[i]
        item = {'cost': int(re.findall('(?<!\+)[0-9]+', item)[0]),
                'damage': int(re.findall('(?<!\+)[0-9]+', item)[1]),
                'armor': int(re.findall('(?<!\+)[0-9]+', item)[2])}
        category[i] = item
    return category

def buildKitQueue(weapons, armors, rings):
    kits = []
    for i in weapons:
        for j in range(-1, len(armors)):
            if j == -1:
                kits.append((i['cost'], i['damage'], 0))
                for k in range(0, len(rings)):
                    kits.append((i['cost']+rings[k]['cost'], i['damage']+rings[k]['damage'], rings[k]['armor']))
                    for l in range(k+1, len(rings)):
                        kits.append((i['cost']+rings[k]['cost']+rings[l]['cost'], i['damage']+rings[k]['damage']+rings[l]['damage'], rings[k]['armor']+rings[l]['armor']))
            else:
                kits.append((i['cost']+armors[j]['cost'], i['damage'], armors[j]['armor']))
                for k in range(0, len(rings)):
                    kits.append((i['cost']+armors[j]['cost']+rings[k]['cost'], i['damage']+rings[k]['damage'], armors[j]['armor']+rings[k]['armor']))
                    for l in range(k+1, len(rings)):
                        kits.append((i['cost']+armors[j]['cost']+rings[k]['cost']+rings[l]['cost'], i['damage']+rings[k]['damage']+rings[l]['damage'], armors[j]['armor']+rings[k]['armor']+rings[l]['armor']))

    return sorted(kits)

def userWins(user, enemy):
    userHitPoints = user[0]
    enemyHitPoints = enemy[0]
    userAttacks = max(user[1]-enemy[2], 1)
    enemyAttacks = max(enemy[1]-user[2], 1)
    userRounds = math.ceil(userHitPoints/enemyAttacks)
    enemyRounds = math.ceil(enemyHitPoints/userAttacks)
    return userRounds >= enemyRounds

store = open('Day 21\\store.txt', 'r').read().split('\n\n')
kits = buildKitQueue(*list(map(formatStoreItems, store)))
enemy = tuple(map(int, re.findall('[0-9]+', open('Day 21\\enemy.txt','r').read())))

for i in kits:
    cost = i[0]
    if userWins((100, i[1], i[2]), enemy):
        print(f'Part 1: {cost}')
        break

kits.reverse()
for i in kits:
    cost = i[0]
    if not userWins((100, i[1], i[2]), enemy):
        print(f'Part 2: {cost}')
        break