        
import time

def e206():
    sevens_number = 7 + 10 ** 8
    sevens_number_squared = sevens_number ** 2
    while sevens_number_squared < 2 * 10 ** 16:
        sevens_squared_str = str(sevens_number_squared)

        if ( sevens_squared_str[0] == '1' and sevens_squared_str[2] == '2' and 
                sevens_squared_str[4] == '3' and sevens_squared_str[6] == '4' and 
                sevens_squared_str[8] == '5' and sevens_squared_str[10] == '6' and 
                sevens_squared_str[12] == '7' and sevens_squared_str[14] == '8' and 
                sevens_squared_str[16] == '9' ):
            return sevens_number * 10

        sevens_number += 10
        sevens_number_squared = sevens_number ** 2

    threes_number = 3 + 10 ** 8
    threes_number_squared = threes_number ** 2
    while threes_number_squared < 2 * 10 ** 16:
        threes_squared_str = str(threes_number_squared)

        if ( threes_squared_str[0] == '1' and threes_squared_str[2] == '2' and 
                threes_squared_str[4] == '3' and threes_squared_str[6] == '4' and 
                threes_squared_str[8] == '5' and threes_squared_str[10] == '6' and 
                threes_squared_str[12] == '7' and threes_squared_str[14] == '8' and 
                threes_squared_str[16] == '9' ):
            return threes_number * 10

        threes_number += 10
        threes_number_squared = threes_number ** 2

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 206 solution is:",  e206()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
