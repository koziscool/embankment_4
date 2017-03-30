        
import time

def e29():
    distinct_set_powers = set()
    for a in xrange( 2, 101 ):
        for b in xrange( 2, 101 ):
            distinct_set_powers.add( a ** b)
    return len(distinct_set_powers)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 29 solution is:",  e29()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
