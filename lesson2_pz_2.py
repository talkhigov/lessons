while True:
    num = int(input('Введите число от 0 до 10: '))
    if num > 0 and num < 10:
        print('возведем в степень 2: ', num ** 2)
        break
    else:
        print('Число должно быть > 0 и < 10')