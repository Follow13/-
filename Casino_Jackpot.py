import random
lot = ['банан', 'клубника', 'арбуз', 'груша', 'персик', 'вишня', 'лимон']
def game_Jackpot():
    print(f'Добро пожаловать на игру джекпот')
    money = int(input('Сколько у вас денег с собой? '))    
    while True:
        rate = int(input('Чтобы сыграть введите стоимость ставки '))
        if rate >= 0:
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
            else:
                pass
            if money == 0:
                break