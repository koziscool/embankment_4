        
import time

def e14():
    collatz_length_dict = { 
        1: 0,
        2: 1,
        4: 2
    }

    def collatz_length( n ):
        if n in collatz_length_dict:
            return collatz_length_dict[n]
        else:
            answer = collatz_length( n//2 ) + 1 if n%2 == 0 else collatz_length( 3*n + 1 ) + 1
            collatz_length_dict[n] = answer
            return answer

    for i in xrange(1, 10 ** 6):
        collatz_length(i)

    return  max(collatz_length_dict, key=collatz_length_dict.get)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 14 solution is:",  e14()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
