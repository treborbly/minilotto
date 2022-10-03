

from codecs import raw_unicode_escape_encode
from multiprocessing.resource_sharer import stop
import random
import math


set = ['x', 'y', 'z']

prize_generator = ''

reward = ''

money_pool = ''


class pool:
    def prize_pool(reward):
        prize_generator = random.randint(1000000, 5000000)

        reward = prize_generator

        print('The lotto has started!, the prize for this lotto is', reward)

    def welcome(reward):
        
        welcome = print('Welcome to the lotto today!')


pool_int = pool()
pool.prize_pool(reward)
pool.welcome(reward)
    



def main():
    while True:
        rand_one = random.randint(1, 3)
        rand_two = random.randint(1, 3)
        rand_three = random.randint(1, 3)
        set = [rand_one, rand_two, rand_three]
        bet_one = input('Enter your first digit (1-3): ')
        bet_two = input('Enter your second digit (1-3): ')
        bet_three = input('Enter your final digit (1-3): ')
        bets = [int(bet_one), int(bet_two), int(bet_three)]

        if bet_one or bet_two or bet_three != 1 or 2 or 3:
            print('Sorry, your digit entry is invalid')
            break
        

        if set == bets:
            print('You have won the lotto!')
            print('Your numbers are', bets)
            print('The winning numbers are', set)
            print('Congratulations!')
            break
        elif set[0] != bets[0] or set[1] != bets[1] or set[2] != bets[2]:
            print('You have lost the lotto.')
            print('Your numbers are', bets)
            print('The winning numbers are', set)
            break

main()

print('Thank you for participating in the lotto.')

def restarter():
    while True:
        restart = input('Would you like to participate in another lotto? (yes or no): ')
        if restart == 'yes':
            pool.prize_pool(reward)
            main()
            continue
        elif restart == 'no':
            print('Thank you and good bye!')
            break


restarter()