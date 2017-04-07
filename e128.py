        
import time

def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
  
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
  
    return found

def e128():

    primes = [2]
    three_prime_diff_neighbors = [1, 2, 8]
    hex_number = lambda n: 3*n*n - 3*n + 1

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

    build_primes_up_to( 10 ** 3 )

    i = 3
    hex_minus_two, hex_minus_one, hex_this_index, hex_plus_one, hex_plus_two = 1, 7, 19, 37, 61

    while True:
        while primes[-1] < hex_plus_two - hex_this_index:
            build_primes_up_to( 2 * primes[-1] )

        if binary_search( primes, hex_this_index - hex_minus_two - 1 ):
            if binary_search( primes, hex_this_index - hex_minus_one - 1 ):
                if binary_search( primes, hex_plus_one - hex_this_index- 1  ):
                    three_prime_diff_neighbors.append( hex_this_index )

        if binary_search( primes, hex_plus_two - hex_this_index - 1 ):
            if binary_search( primes, hex_plus_one + 1 - hex_this_index  ):
                if binary_search( primes, hex_plus_one - hex_this_index - 1  ):
                    three_prime_diff_neighbors.append( hex_this_index + 1)

        if len(three_prime_diff_neighbors) == 2000:
            return three_prime_diff_neighbors[-1]

        i += 1
        (hex_minus_two, hex_minus_one, hex_this_index, hex_plus_one, hex_plus_two)  = \
            (hex_minus_one, hex_this_index, hex_plus_one, hex_plus_two, hex_number(i+2) )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 128 solution is:",  e128()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
