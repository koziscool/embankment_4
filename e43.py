
from itertools import permutations        
import time

def e43():
    digit_list = map( lambda n:str(n), range(0, 10) )
    total_divisible_substrings = 0
    for perm in permutations(digit_list):
        perm_str = ''.join(perm)
        if ( int(perm_str[7:10]) % 17 == 0 and 
                int(perm_str[6:9]) % 13 == 0 and
                int(perm_str[5:8]) % 11 == 0 and 
                int(perm_str[4:7]) % 7 == 0 and
                int(perm_str[3:6]) % 5 == 0 and
                int(perm_str[2:5]) % 3 == 0 and
                int(perm_str[1:4]) % 2 == 0
            ):
            total_divisible_substrings += int(perm_str)

    return total_divisible_substrings

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 43 solution is:",  e43()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
