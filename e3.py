
import time

def e3():

    input_number, primes_limit = 600851475143, 10 ** 6

    def primes_up_to( limit ):
        primes = [2]
        current_counter = 3

        while primes[-1] < limit:
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

        primes.pop()
        return primes


    def factorize( num, primes ):
        factors = []
        primes_index = 0
        currentQuotient = num
        while currentQuotient > 1:
            p = primes[ primes_index ]
            while currentQuotient % p == 0:
                currentQuotient /= p
                factors.append(p)
            primes_index += 1
        return factors

    primes =  primes_up_to(primes_limit)
    factors = factorize( input_number, primes )
    return max(factors)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 3 solution is:",  e3()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
                