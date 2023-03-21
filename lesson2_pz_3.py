first_name = input('Имя: ')
last_name = input('Фамилия: ')
age = int(input('Возраст: '))
weight = int(input('Вес: '))

if age < 30 and weight >= 50 and weight < 120:
    print(f'{first_name} {last_name}, {age} год, вес: {weight} - хорошее состояние')
elif age >= 30 and age <= 40 and (weight < 50 or weight > 120):
    print(f'{first_name} {last_name}, {age} год, вес: {weight} - требуется заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print(f'{first_name} {last_name}, {age} год, вес: {weight} - требуется врачебный осмотр')
elif age < 30 and weight > 120:
    print(f'{first_name} {last_name}, {age} год, вес: {weight} - требуется врачебный осмотр')
