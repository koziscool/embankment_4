        
import time
from math import floor, sqrt

range_dict = {}

def e135():
    # for n in xrange(1, 10 ** 4 ):
    n = 1155
    for a in xrange(1, int(sqrt(n)) + 1):
        b = n / float(a)
        if b == n / a:
            k = (a + b) / 4.0
            h = (5*a + b) / 4.0
            if k == floor(k):
                print h, k
                if n in range_dict:
                    range_dict[n] += 1
                else:
                    range_dict[n] = 1

    print range_dict
    # print range_dict[1155]
    # one_soln = filter( lambda x:range_dict[x] == 10, range_dict.keys())
    # print len(one_soln), len(range_dict)
    return 'not ready'

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 135 solution is:",  e135()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
