        

import time

def e50():

    primes, current_counter, limit = [2], 3, 10

    while primes[-1]  < limit:
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

    max_prime_sum = 1
    for p in primes:
        current_index = primes.index(p)
        p_sum, current_prime = p, p
        while  current_index < len(primes) and p_sum in primes:
            if p_sum > max_prime_sum:
                max_prime_sum = p_sum
            print p, current_prime, p_sum, max_prime_sum
            current_index += 1
            current_prime = primes[current_index]
            p_sum += current_prime

    return max_prime_sum

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 50 solution is:",  e50()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
