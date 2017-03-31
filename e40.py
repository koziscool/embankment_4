         
import time

def e40():
    limit = 10 ** 6
    s = ' ' + ''.join(map( lambda n: str(n), xrange(1, limit + 1)))
    return (int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) *
             int(s[10000]) * int(s[100000]) * int(s[1000000]) )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 40 solution is:",  e40()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
