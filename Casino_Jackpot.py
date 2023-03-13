import random
rate = 10
money = 100
print(f'Добро пожаловать на игру джекпот, стоимость ставки {rate}$')
lot = ['банан', 'клубника', 'арбуз', 'груша', 'персик', 'вишня', 'лимон']
while True:
    play = int(input('Чтобы сыграть введите стоимость ставки '))
    if play == 10:
        money -= 10
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
        print(f' У вас на счету {money}$')
        if money == 0:
            break
