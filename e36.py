        
import time

def e36():

    def is_pal( n ):
        return str(n) == str(n)[::-1]

    def binary_str( n ):
        quotient, remainder, ret_str = n, 0, ''
        while quotient > 0:
            ret_str = str(quotient % 2) + ret_str
            quotient /= 2
        return ret_str

    limit = 10 ** 6
    result = filter( lambda n: is_pal(n) and is_pal(binary_str(n)), xrange(1, limit))
    return sum(result)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 36 solution is:",  e36()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
