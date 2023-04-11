import random
lot = ['банан', 'клубника', 'арбуз', 'груша', 'персик', 'вишня', 'лимон']

def game_Jackpot():
    global money
    print(f'Добро пожаловать на игру джекпот')
    try:    
        money = int(input('Сколько у вас денег с собой? '))
    except ValueError:
        print('Введите число, а не буквы') 
        game_Jackpot()   
    while True:
        try:    
            rate = int(input('Чтобы сыграть введите стоимость ставки, если хотите уйти введите "1" '))
        except ValueError:
            print('Введите число, а не буквы')
            continue
        if rate == 1:
            break
        elif rate >= 0:
            money -= rate
            print(f'У вас на счету {money}$')
            lot1 = random.randint(0, 6)
            lot2 = random.randint(0, 6)
            lot3 = random.randint(0, 6)
            print(f'\t{lot[lot1]}')
            print(f'\t{lot[lot2]}')
            print(f'\t{lot[lot3]}')
            if lot1 == lot2 == lot3:
                print(f'Вы выиграли и получили {rate * 10}$')
                money += rate * 10
            elif lot1 == lot2 or lot2 == lot3 or lot1 == lot3:
                print(f'Вы выиграли и получили {rate * 2}$')
                money += rate * 2
                print(f'У вас {money}')
            else:
                pass
            if money == 0:
                break
        elif rate == 50:
            break