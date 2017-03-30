        
import time

def build_primes_up_to(n):
    primes = [2]
    current_counter = 3
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

    primes.pop()
    return primes

def shift_digits(n):
    return int(str(n)[-1] + str(n)[0:-1] )

def e35():
    limit = 10 ** 6
    primes = build_primes_up_to( limit )
    circular_primes = []
    for p in primes:
        str_digits = str(p)
        if len(str_digits) == 1:
            circular_primes.append( p )
        else:
            if '0' in str_digits or '2' in str_digits or '4' in str_digits or '6' in str_digits or '8' in str_digits:
                continue
            is_circular, current_number = True, p
            for i in xrange( 1, len(str_digits) ):
                current_number = shift_digits( current_number )
                if current_number not in primes:
                    is_circular = False
                    break
            if is_circular:
                circular_primes.append( p )

    return len(circular_primes)


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 35 solution is:",  e35()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
