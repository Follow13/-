from Casino_roulette import *
from Casino_Jackpot import *

def say_hi(): 
    print('Приветствую в казино "7 Бананов"')

def offer_play():
    print('Рулетка')
    print('Джекпот')
    offer = input('В какую игру хотите сыграть? ').lower()
    if offer == 'рулетка':
        game_roulette()
    elif offer == 'джекпот':
        game_Jackpot()
    else:
        pass
say_hi()
offer_play()
def exit(rate, money1):
    if rate == 1 or money1 == 0:
        offer_play()
exit(rate = 1, money1 = 0)


