        
import time

def unit_fraction_expansion_length(  i ):
    expansion = []
    current_tuple = (1, 0)
    dividend = 1
    decimal = 0
    while current_tuple not in expansion:
        expansion.append(current_tuple)
        dividend *= 10
        decimal = dividend / i 
        dividend = dividend % i 
        current_tuple = dividend, decimal
    
    return len(expansion) -  expansion.index( current_tuple )


def e26():
    max_expansion_length, max_index = 1, 0
    for i in xrange(1, 1000):
        expansion_length = unit_fraction_expansion_length( i )
        if max_expansion_length < expansion_length:
            max_expansion_length = expansion_length
            max_index = i 
    
    return max_index

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 26 solution is:",  e26()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
