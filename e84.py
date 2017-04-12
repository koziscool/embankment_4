
import time
from random import randint
from collections import defaultdict

def e84():
    NUM_SQUARES = 40
    six_dice_throw = lambda: (randint(1, 6), randint(1, 6))
    four_dice_throw = lambda: (randint(1, 4), randint(1, 4))
    board = range(0, NUM_SQUARES + 1)
    current_square, current_roll_double, prev_roll_double, prevx2_roll_double = 0, False, False, False
    chance_card_number, cc_card_number, NUM_CARDS = 0, 0, 16

    frequency_dict = defaultdict(lambda: 0)
    NUM_TURNS = 5 * 10** 6
    for i in xrange(NUM_TURNS):

        d1, d2 = four_dice_throw()
        current_square = ( current_square + d1 + d2 ) % NUM_SQUARES

        # monopoly rules here
        # three consecutive doubles = jail
        current_roll_double = (d1 == d2)
        if current_roll_double and prev_roll_double and prevx2_roll_double:
            current_square = 10
            prev_roll_double, prevx2_roll_double = False, False

        # go to jail
        if current_square == 30:
            current_square = 10
            prev_roll_double, prevx2_roll_double = False, False

        # community chest
        if current_square == 2 or current_square == 17 or current_square == 33:
            if cc_card_number == 1:
                current_square = 10
                prev_roll_double, prevx2_roll_double = False, False
            if cc_card_number == 2:
                current_square = 0
            cc_card_number = (cc_card_number + 1) % 16

        #chance
        if current_square == 7 or current_square == 22 or current_square == 36:
            if chance_card_number == 1:
                current_square = 10
                prev_roll_double, prevx2_roll_double = False, False
            if chance_card_number == 2:
                current_square = 0
            if chance_card_number == 3:
                current_square = 11
            if chance_card_number == 4:
                current_square = 24
            if chance_card_number == 5:
                current_square = 5
            if chance_card_number == 6:
                current_square = 39                
            if chance_card_number == 7:
                if current_square == 7 or current_square == 36:
                    current_square = 12
                if current_square == 22:
                    current_square = 28
            if chance_card_number == 8 or chance_card_number == 9:
                if current_square == 7:
                    current_square = 15
                if current_square == 22:
                    current_square = 25
                if current_square == 36:
                    current_square = 5
            if chance_card_number == 10:
                current_square -= 3
        chance_card_number = (chance_card_number + 1) % NUM_CARDS

        frequency_dict[current_square] += 1
        prev_roll_double, prevx2_roll_double = current_roll_double, prev_roll_double

    sorted_squares = [key for key in sorted(frequency_dict, key=frequency_dict.__getitem__, reverse=True) ]
    return str(sorted_squares[0]) + str(sorted_squares[1]) + str(sorted_squares[2])

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 84 solution is:",  e84()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


