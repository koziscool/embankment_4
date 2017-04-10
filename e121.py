        
import time
import operator

def e121():
    NUM_TURNS = 15
    prod = lambda arr: reduce( operator.mul, arr, 1)
    blue_wins = lambda arr: len(filter( lambda c: c == '1', arr)) > NUM_TURNS / 2
    blue_probability = 0

    for i in xrange(2 ** NUM_TURNS):
        b_format = '0' + str(NUM_TURNS) +'b'
        bin_str = format( i, b_format)

        if blue_wins( bin_str ):
            blue_probability += prod( map( lambda c, k: 1.0/(k +2) if c == '1' else  (k + 1.0)/(k +2), bin_str, xrange(NUM_TURNS) ) )

    return int( 1 / blue_probability )


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 121 solution is:",  e121()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
