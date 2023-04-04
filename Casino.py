from Casino_roulette import *
from Casino_Jackpot import *
from Casino_BlackJack import *

def say_hi(): 
    print('Приветствую в казино "7 Бананов"')

def offer_play():
    print('Рулетка')
    print('Джекпот')
    print('Блекджек')
    offer = input('В какую игру хотите сыграть? ').lower()
    if offer == 'рулетка':
        game_roulette()
    elif offer == 'джекпот':
        game_Jackpot()
    elif offer == 'блекджек':
        game_BlackJack()
    else:
        pass
say_hi()
offer_play()
def exit(rate, money1, bet):
    if rate == 1 or money1 == 0 or bet == 0:
        offer_play()
exit(rate = 1, money1 = 0, bet = 0)


