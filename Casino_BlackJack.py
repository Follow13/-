import random
cards = ['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠', '2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣',
         '2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥', '2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦',
         'j♠','q♠','k♠', 'j♣','q♣','k♣', 'j♥','q♥','k♥', 'j♦','q♦','k♦', 'a♠', 'a♣','a♥','a♦']
pic = ['j', 'q', 'k']

def check_card(lot):
    global hand, total
    if lot[0] in pic or lot[1] == '0':
        total += 10
    elif lot[0] == 'a':
        if total <= 10:
            total += 11
        else:
            total += 1
    else:
        total += int(lot[0])
    hand.append(lot)

def check_bot(lot_bot):
    global hand_bot, total_bot
    if lot_bot[0] in pic or lot_bot[1] == '0':
        total_bot += 10
    elif lot_bot[0] == 'a':
        if total_bot <= 10:
            total_bot += 11
        else:
            total_bot += 1
    else:
        total_bot += int(lot_bot[0])
    hand_bot.append(lot_bot)

def game_BlackJack():
    global hand, total, hand_bot, total_bot
    print(f'Добро пожаловать на игру Блекджек')
    try:    
        money = int(input('Сколько у вас денег с собой? '))
    except ValueError:
        print('Введите число, а не буквы')
        game_BlackJack()
    while True:
        if money <= 0:
            print('Деньги закончились')
            break
        hand = []
        hand_bot = []
        total = 0
        total_bot = 0    
        try:    
            bet = int(input('Ваша ставка, если хотите уйти введите 0 '))
        except ValueError:
            print('Введите число, а не буквы')
            continue
        if bet == 0:
            break
        money -= bet
        lot1 = random.choice(cards)
        check_card(lot=lot1)
        lot2 = random.choice(cards)
        check_card(lot=lot2)
        
        lot1_bot = random.choice(cards)
        check_bot(lot_bot=lot1_bot)
        lot2_bot = random.choice(cards)
        check_bot(lot_bot=lot2_bot)
        print(f'Ваши карты {lot1}, {lot2}')
        print(f'Карты дилера {lot1_bot}, {lot2_bot}')
        
        while True:
            if total < 21:
                answer = input('Добавить карту? ').lower()
                if answer == 'да':
                    next_lot = random.choice(cards)
                    check_card(next_lot)
                    print(f'Ваши карты {hand}. Вы набрали {total}')
                    continue
                elif answer == 'нет':
                    print(f'Ваши карты {hand}. Вы набрали {total}')
                
                if total_bot < 17:
                    next_lot_bot = random.choice(cards)
                    check_bot(next_lot_bot)
                    print(f'Карты у дилера {hand_bot}. Он набрал {total_bot}')
                elif total_bot >= 17:
                    print(f'Карты у дилера {hand_bot}. Он набрал {total_bot}')
                elif total_bot == 21:
                    print(f'Карты у дилера {hand_bot}. Он набрал {total_bot}')
                    print('Дилер выиграл')
                    break
                else:
                    print(f'Карты у дилера {hand_bot}. Он набрал {total_bot}')
            if 21 >= total > total_bot:
                print(f'Ваши карты {hand}, Вы набрали {total}')
                print('Вы выиграли')
                money += bet * 1.5
                print(money)
                break
            elif total < total_bot <= 21:
                print('Выиграл дилер')
                print(money)
                break

            if total == 21:
                print(f'Ваши карты {hand}, Вы набрали {total}')
                print('Вы выиграли')
                money += bet * 1.5
                print(money)
                break
            else:
                print(f'Ваши карты {hand}. Вы набрали {total}')
                print(f'Карты у дилера {hand_bot}. Он набрал {total_bot}')
                print(money)
                break
            