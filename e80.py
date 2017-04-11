
import time
from decimal import Decimal, getcontext
from math import sqrt
getcontext().prec = 110

def e80():
    total_digits = 0
    for a in range(1, 100):
        if not sqrt(a) % 1 == 0:
            ans = str(Decimal(a).sqrt()).replace('.', '')[:100]
            total_digits += sum(map(int, ans))
    return total_digits
    
if __name__ == "__main__":
    start = time.time()
    print
    e80()
    print "Euler 80 solution is:",  e80()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


