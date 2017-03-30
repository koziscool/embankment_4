        
import time

def sum_spiral_ring(n):
    if n == 1:
        return 1
    if n%2 != 1:
        return
    increment = n-1
    return n*n + (n*n - increment) + (n*n - 2 * increment) + (n*n - 3 * increment)

def e28():
    spiral_size = 1001
    return sum( map(sum_spiral_ring, xrange(1, spiral_size + 1, 2) ) )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 28 solution is:",  e28()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
