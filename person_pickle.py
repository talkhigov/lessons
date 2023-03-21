import pickle

person = {
    'first_name': 'Ilman',
    'last_name': 'Талхигов',
    'age': 20,
    'from': 'Russia',
    'phone': 'apple iphone X',
    'devoloper': 'Python'
}

with open('person.pickle', 'wb') as f:
    pickle.dump(person, f)

print('готово')
print(type(person))

with open('person.pickle', 'rb') as f:
    person = pickle.load(f)

print(person)