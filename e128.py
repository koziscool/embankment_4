        
import time

hex_tuples = {}
hex_values = {}

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


def neighbors( n ):
    def corner_tuple_neighbors( n_tuple ):
        ret_tuples = []
        if n_tuple[0] == 1:
            ret_tuples.append( (0, 0, 0) )
            ret_tuples.append( (n_tuple[0], (n_tuple[1] + 1) % 6, 0) )
            ret_tuples.append( (n_tuple[0], (n_tuple[1] - 1) % 6, 0) )
        else:
            ret_tuples.append( (n_tuple[0] - 1, n_tuple[1], 0) )
            ret_tuples.append( (n_tuple[0], n_tuple[1], n_tuple[2] +1) )
            ret_tuples.append( (n_tuple[0], (n_tuple[1] - 1) % 6, -1 % n_tuple[0] ) )


        ret_tuples.append( (n_tuple[0] + 1, n_tuple[1], 0) )
        ret_tuples.append( (n_tuple[0] + 1, n_tuple[1], 1) )
        ret_tuples.append( (n_tuple[0] + 1, (n_tuple[1] - 1) % 6, -1 % (n_tuple[0] + 1) ))

        return ret_tuples

    def side_tuple_neighbors( n_tuple ):
        ret_tuples = []
        ret_tuples.append( (n_tuple[0], n_tuple[1], n_tuple[2] - 1) )
        ret_tuples.append( (n_tuple[0] + 1 , n_tuple[1], n_tuple[2]) )
        ret_tuples.append( (n_tuple[0] + 1, n_tuple[1], n_tuple[2] + 1) )

        if n_tuple[2] == n_tuple[0] - 1:
            ret_tuples.append( (n_tuple[0], (n_tuple[1] + 1) % 6, 0) )
            ret_tuples.append( (n_tuple[0] -1, (n_tuple[1] + 1) % 6, 0) )
        else:
            ret_tuples.append( (n_tuple[0], n_tuple[1], n_tuple[2] + 1) )
            ret_tuples.append( (n_tuple[0] - 1, n_tuple[1], n_tuple[2]) )

        ret_tuples.append( (n_tuple[0] - 1, n_tuple[1], n_tuple[2] - 1) )

        return ret_tuples

    n_tuple = hex_tuples[n]
    side_len = n_tuple[0]
    if n_tuple[0]  == 0:
        neighbor_tuples = filter( lambda tp: tp[0] == 1, hex_values.keys())
    else:
        if n_tuple[2] == 0:
            neighbor_tuples = corner_tuple_neighbors( n_tuple )
        else:
            neighbor_tuples = side_tuple_neighbors( n_tuple )

    neighbors = map( lambda tp: hex_values[tp], neighbor_tuples )
    return  neighbors

def build_hex( num_rings ):
    hex_tuples[1], hex_values[(0, 0, 0)] = (0, 0, 0), 1
    current_counter = 1
    for ring in xrange(1, num_rings):
        side_len = ring
        for direction in xrange(0, 6):
            for side in xrange(0, side_len):
                current_counter += 1
                hex_tuples[current_counter] = (ring, direction, side)
                hex_values[(ring, direction, side)] = current_counter

def e128():
    limit_prime_diff_neighbors = 10
    primes = build_primes_up_to( 10 ** 4 )
    build_hex(1000)
    three_prime_diff_neighbors = []
    for hex_tile in xrange( 1, 10 ** 6 ):
        hex_neighbors = neighbors( hex_tile )
        num_prime_diff_neighbors = 0
        for n in hex_neighbors:
            diff = abs( hex_tile - n )
            if diff in primes:
                num_prime_diff_neighbors += 1
        if num_prime_diff_neighbors == 3:
            three_prime_diff_neighbors.append( hex_tile)

        if len(three_prime_diff_neighbors) == limit_prime_diff_neighbors:
            break

    print len(three_prime_diff_neighbors)
    return three_prime_diff_neighbors[-1]

    # build_hex(20)
    # for i in xrange(0, 15):
    #     little_tuple, big_tuple = (i, 0, 0), (i+1, 0, 0)
    #     print hex_values[big_tuple] - hex_values[little_tuple]
    #     # print hex_tuples[i]


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 128 solution is:",  e128()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
