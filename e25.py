        
import time

def e25():
    fibo = [1, 1]
    while len(str( fibo[-1] )) <  1000:
        fibo.append( fibo[-1] + fibo[-2] )

    return len(fibo)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 25 solution is:",  e25()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
