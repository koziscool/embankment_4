
import time

def e2():
    total = 0
    previous_f, current_f = 1, 2
    while current_f < 4 * 10 ** 6:
        if current_f % 2 == 0:
            total += current_f
        previous_f, current_f = current_f, current_f + previous_f
    return total


if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 2 solution is:",  e2()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
