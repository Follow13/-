import random
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
min = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
max = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
zero = 0
rate = 10
money = 100
lot = random.randint(0, 36)
while True:
    print('Время ставок! \nКаждая ставка равна 10$ \nЕсли вы хотите пропустить ставку введите любую букву или число, где это требуется.')
    print(f'У вас {money}$')
    color = input('Ставка на красное или чёрное ')
    number = int(input('Ставка на определённое число '))
    minmax = int(input('Ставка на число от 1 до 18 или от 19 до 36 (1 или 2) '))
    if color == 'красное':
        money -= 10
    elif color == 'чёрное':
        money -= 10
    else:
        pass
    if number >= 0 and number <= 36:
        money -= 10
    else:
        pass
    if minmax == 1:
        money -= 10
    elif minmax == 2:
        money -= 10
    else:
        pass
    print(f'У вас {money}')
    
    if lot == zero:
        print('Выпало число 0!')
        if number == lot:
            print('Вы выиграли')
            money += rate * 100
    else:
        print(f'Выпавший номер: {lot}')
        if lot in red:
            print('Выигравшая ставка: красное')
            if color == 'красное':
                print('Ставка зашла')
                money += rate * 2
        elif lot in black:
            print('Выигравшая ставка: чёрное')
            if color == 'чёрное':
                print('Ставка зашла')
                money += rate * 2
        if lot in min:
            print('Выигравшая ставка: от 1 до 18')
            if minmax == 1:
                print('Ставка зашла')
                money += rate * 2
        elif lot in max:
            print('Выигравшая ставка: от 19 до 36')
            if minmax == 2:
                print('Ставка зашла')
                money += rate * 2
        if lot % 2 == 0:
            print('Выигравшая ставка: чётное')
            if number % 2 == 0:
                print('Ставка зашла')
                money += rate * 2
        elif lot % 2 == 0:
            print('Выигравшая ставка: нечётное')
            if number % 2 != 0:
                print('Ставка зашла')
                money += rate * 2

