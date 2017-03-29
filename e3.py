
import time

def e3():
    return 'not ready'

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 3 solution is:",  e3()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
                