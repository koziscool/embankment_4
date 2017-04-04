        
import time

range_dict = {}

def e136():
    my_func = lambda h, k: 6*h*k - h*h -5*k*k

    for k in xrange(1, 15000 ):
        for h in xrange( 2*k + 1, 6*k ):
            mf = my_func(h, k)
            if mf > 0:
                if mf in range_dict:
                    range_dict[mf] += 1
                else:
                    range_dict[mf] = 1

    print range_dict[20]
    one_soln = filter( lambda x:range_dict[x] == 1 and x > 0 and x < 5 * 10 ** 7, range_dict.keys())
    print len(one_soln), len(range_dict)
    return 'not ready'

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 136 solution is:",  e136()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
