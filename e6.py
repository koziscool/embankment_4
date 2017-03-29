
import time

def e6():
    end_val = 100
    square_sum = sum( xrange(1, end_val+1) ) ** 2
    sum_squares = sum( map( lambda x: x*x, xrange(1, end_val+1) ) )
    return square_sum - sum_squares

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 6 solution is:",  e6()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
