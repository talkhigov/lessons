def num():
    number = int(input('Введите число от 1 до 100: '))
    if number <= 0 or number > 100:
        print('число должно быть от 1 до 100')
    elif number == 13:
        try:
            print(ValueError)
            print('исключительная ситуация.\nВведите другое число.')
        except ValueError:
            print('исключительная ситуация.\nВведите другое число')
    else:
        print(number**2)


num()