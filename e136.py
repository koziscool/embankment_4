        
import time
from math import floor 

# range_dict = {}
primes = [2]
# prime_factors = { 2: {2:1} }
# distinct_factors = { 1: [1], 2: [1, 2] }


def build_primes_up_to(n):
    current_counter = primes[-1] + 1
    while current_counter <= n:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append( current_counter )
        current_counter += 1

def e136():
    limit = 5 * 10 ** 7
    build_primes_up_to( limit )
    num_unique_solns = 2
    for p in primes[1:]:
        if p < limit / 4:
            num_unique_solns += 1
        if p <  limit / 16:
            num_unique_solns += 1
        if (p - 3) % 4 == 0:
            num_unique_solns += 1

    return num_unique_solns 

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 136 solution is:",  e136()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
