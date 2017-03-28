

import time

def e1():
    ret_val = 0
    for i in xrange( 1000 ):
        if i % 3 == 0 or i % 5 == 0:
            ret_val += i
    return ret_val
    
if __name__ == "__main__":
    start = time.time()
    # print
    print
    print "Euler 1 solution is:",  e1()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


