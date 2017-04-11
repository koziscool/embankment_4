

import time
import math

x = math.sqrt(2)

print format(x, '.100f')

def e80():
    return 'koz'
    
if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 80 solution is:",  e80()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


