        
import time

def e20():
    factorial = lambda n: reduce( lambda x, y: x*y, xrange(1, n+1) )
    return sum( map(lambda c: int(c), str( factorial(100) )))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 20 solution is:",  e20()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
