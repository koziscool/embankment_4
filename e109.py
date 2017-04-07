        
import time

def e109():
    doubles_dict = {
      'd1': 2, 'd2':4, 'd3': 6, 'd4': 8, 'd5': 10, 'd6': 12, 'd7': 14, 'd8': 16, 'd9': 18, 'd10': 20, 
      'd11': 22, 'd12':24, 'd13': 26, 'd14': 28, 'd15': 30, 'd16': 32, 'd17': 34, 'd18': 36, 'd19': 38, 'd20': 40,
      'db': 50
    }

    others_dict = {
      's1': 1, 's2':2, 's3': 3, 's4': 4, 's5': 5, 's6': 6, 's7': 7, 's8': 8, 's9': 9, 's10': 10, 
      's11': 11, 's12': 12, 's13': 13, 's14': 14, 's15': 15, 's16': 16, 's17': 17, 's18': 18, 's19': 19, 's20': 20,
      'sb': 25,  
      't1': 3, 't2':6, 't3': 9, 't4': 12, 't5': 15, 't6': 18, 't7': 21, 't8': 24, 't9': 27, 't10': 30, 
      't11': 33, 't12':36, 't13': 39, 't14': 42, 't15': 45, 't16': 48, 't17': 51, 't18': 54, 't19': 57, 't20': 60,
    }

    combined_dict = doubles_dict.copy()
    combined_dict.update(others_dict)

    checkouts = {}

    for fk, fv in combined_dict.items():
        for sk, sv in combined_dict.items():
            for tk, tv in doubles_dict.items():
                if (sk, fk, tk) not in checkouts:
                    checkouts[(fk, sk, tk)] = fv + sv + tv

    for fk, fv in combined_dict.items():
        for sk, sv in doubles_dict.items():
            checkouts[(fk, sk)] = fv + sv

    for fk, fv in doubles_dict.items():
        checkouts[(fk)] = fv

    return len( filter( lambda v: v < 100, checkouts.values() ))


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 109 solution is:",  e109()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
