import random

cars = ['audi', 'porshe', 'polo', 'lada']
lst = []

def items_random(val):
    if val == []:
        return None
    else:
        return random.choice(val)

# print(items_random(lst))