player = {
    # 'name': input('Введите имя: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

player2 = {
    'name': 'Morti',
    'health': 150,
    'damage': 100,
    'armor': 1.2
}

player3 = {
    'name': 'Mort',
    'health': 50,
    'damage': 200,
    'armor': 1.2
}

enemy = {
    'name': 'Elsi',
    'health': 90,
    'damage': 60,
    'armor': 1.2
}

def attack(person1, person2):
    health1 = person2['health'] - person1['damage'] 
    armor1 = person1['damage'] / person2['armor']
    print(person1['name'] + ' нанёс ' + str(person1['damage']) + ' урона ' + person2['name'])
    return f'Жизнь: {health1}\nБроня: {int(armor1)}'
print(attack(player2, player3))