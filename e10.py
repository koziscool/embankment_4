
import time

def e10():
    primes = [2]
    current_counter = 3

    while primes[-1] < 2 * 10 ** 6:
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
    return sum(primes)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 10 solution is:",  e10()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
