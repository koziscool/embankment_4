        
import time
from math import floor 

range_dict = {}
primes = [2]
prime_factors = { 2: {2:1} }
distinct_factors = { 1: [1], 2: [1, 2] }

def build_primes_and_factors_up_to(n):
    current_counter = primes[-1] + 1
    while current_counter <= n:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                prime_factors[current_counter] =  prime_factors[current_counter / p].copy()
                if p in prime_factors[current_counter]:
                    prime_factors[current_counter][p] += 1
                else:
                    prime_factors[current_counter][p] = 1

                df = [1]
                for p in prime_factors[current_counter]:
                    new_df = []
                    for exp in xrange(0, prime_factors[current_counter][p] + 1):
                        for f in df:
                            new_df.append( f * p ** exp )
                    df = new_df
                distinct_factors[current_counter] = df
                break

        if is_prime:
            primes.append( current_counter )
            prime_factors[current_counter] = { current_counter: 1}
            distinct_factors[current_counter] = [1, current_counter]
        current_counter += 1


def e135():
    build_primes_and_factors_up_to( 10 ** 6 )
    for n in xrange(1, 10 ** 6):
        for a in distinct_factors[n]:
            b = n / a
            k = (a + b) / 4.0
            h = (5*a + b) / 4.0
            if h > 2*k and k == floor(k):
                # print h, k, a, b, 6*h*k - h*h - 5*k*k
                if n in range_dict:
                    range_dict[n] += 1
                else:
                    range_dict[n] = 1

    ten_solns = filter( lambda x:range_dict[x] == 10, range_dict.keys())
    return len(ten_solns)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 135 solution is:",  e135()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
