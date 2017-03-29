
import time

def e4():
    def is_pal( n ):
        return str(n) == str(n)[::-1]

    max_product = 0
    for a in xrange(100, 1000):
        for b in xrange(100, 1000):
            if is_pal(a*b) and a*b > max_product:
                max_product = a*b
    return max_product


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 4 solution is:",  e4()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
