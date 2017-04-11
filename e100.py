

import time
import math

def e100():
    k, n = 14, 20
    while n+1 < 10 ** 12:
        k, n = 3*k + 2*n + 2, 4*k + 3*n + 3
    
    return k+1

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 100 solution is:",  e100()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


