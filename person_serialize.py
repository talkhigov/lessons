import json

person = {
    'first_name': 'Ilman',
    'last_name': 'Талхигов',
    'age': 20,
    'from': ['Russia'],
    'phone': 'apple iphone X',
    'devoloper': 'Python'
}

with open('person.json', 'w', encoding='utf-8') as f:
    person = json.dump(person, f)

print('ВЫПОЛНЕНО')
print(type(person))

with open('person.json', 'r', encoding='utf-8') as f:
    print(f.read())