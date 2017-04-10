        
import time
import operator
# import math

def e121():
    NUM_TURNS = 15
    prod = lambda arr: reduce( operator.mul, arr, 1)
    blue_wins = lambda arr: len(filter( lambda c: c == 'B', arr)) > NUM_TURNS / 2
    blue_probability = 0

    for i in xrange(2 ** NUM_TURNS):
        result_array = []
        probability_array = []
        for bit_index in xrange(NUM_TURNS):
            if i & 2**bit_index:
                result_array.append('B')
                probability_array.append( 1.0/(bit_index +2) )
            else:
                result_array.append('R')
                probability_array.append( (bit_index + 1.0)/(bit_index +2) )

        if blue_wins( result_array ):
            blue_probability += prod( probability_array )


    # print blue_probability
    return int( 1 / blue_probability )
    # return 'not ready'

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 121 solution is:",  e121()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
