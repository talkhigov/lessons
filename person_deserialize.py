import json

with open('person.json', 'r', encoding='utf-8') as f:
    print(f.read())

with open('person.pickle', 'r') as f:
    print(f.read())

with open('person.json', 'r', encoding='utf-8') as f:
    person = json.load(f)
print(person)