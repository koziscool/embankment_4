
import time

primes = [2]
prime_factors = { 2: {2:1} }
sum_divisors = { 1:1, 2: 1 }

def build_primes_and_factors_and_find_solutions_up_to(n):
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
                sum_divisors[current_counter] = sum(df) - current_counter
                break

        if is_prime:
            primes.append( current_counter )
            prime_factors[current_counter] = { current_counter: 1}
            sum_divisors[current_counter] = 1
        current_counter += 1

def e95():
    build_primes_and_factors_and_find_solutions_up_to( 10 ** 6 )
    amicable_chains = set()
    amicable_resolved = set()
    for i in xrange(1, 10 ** 6 + 1):
        if i in amicable_resolved:
            continue
        current_elt, current_chain = i, [i]
        while True:
            if sum_divisors[current_elt] > 10 ** 6:
                amicable_resolved.update( current_chain )
                break
            if sum_divisors[current_elt] in current_chain:
                index = current_chain.index( sum_divisors[current_elt] )
                amicable_chains.add( tuple(current_chain[index:]) )
                amicable_resolved.update( current_chain )
                break        
            current_elt = sum_divisors[current_elt]
            current_chain.append(current_elt)

    max_chain_length, min_elt = 0, 0
    for tup in amicable_chains:
        if len(tup) > max_chain_length:
            max_chain_length = len(tup)
            min_elt = min(tup)

    return min_elt


if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 95 solution is:",  e95()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


