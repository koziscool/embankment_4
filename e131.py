
import time

def e131():

    primes = [2]

    def build_primes_up_to(n):
        current_counter = primes[-1] + 1
        while primes[-1] < n:
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

    build_primes_up_to( 10 ** 6 )
    primes.pop()

    i, cube_friendly_primes = 1, []
    while True:
        pp = 3*i*i + 3*i + 1
        if pp > primes[-1]:
            break
        if pp in primes:
            cube_friendly_primes.append(pp)
        i += 1

    return len(cube_friendly_primes)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 131 solution is:",  e131()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))