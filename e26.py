        
import time

def unitFraction(  i):
    expansion = []
    currentTuple = (1, 0)
    dividend = 1
    decimal = 0
    while currentTuple not in expansion:
        expansion.append(currentTuple)
        dividend *= 10
        decimal = dividend / i 
        dividend = dividend % i 
        currentTuple = dividend, decimal
    
    return expansion

print unitFraction(7)

def e26():
    return 'koz'
    # for i in xrange(1, 100):
    #     print i, "%.20f" % (1/float(i)) 

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 26 solution is:",  e26()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
