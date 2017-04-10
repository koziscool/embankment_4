        
import time

def e172():
    limit_num_digits = 18
    total_digit_combos = { 1: 9 }
    digit_pattern_combos = { (1,): 9 }
    digit_pattern_tuples = { 1: [(1,)] }
    
    for index_num_digits in xrange(2, limit_num_digits + 1):
        working_digits_list = digit_pattern_tuples[ index_num_digits - 1]
        digit_pattern_tuples[ index_num_digits ] = []
        for tuple_item in working_digits_list:

            list_item = list(tuple_item)

            if len(tuple_item) < 10:
                list_item_copy = list_item[:]
                list_item_copy.append( 1 )
                new_tuple = tuple( list_item_copy )
                if new_tuple in digit_pattern_tuples[ index_num_digits ]:
                    digit_pattern_combos[new_tuple] += digit_pattern_combos[tuple_item] * (10 - len(tuple_item))
                if ( new_tuple not in digit_pattern_tuples[ index_num_digits ] and new_tuple[0] <=3):
                    digit_pattern_tuples[ index_num_digits ].append( new_tuple )
                    digit_pattern_combos[new_tuple] = digit_pattern_combos[tuple_item] * (10 - len(tuple_item) )

            for i, l in enumerate( list_item ):
                list_item_copy = list_item[:]
                list_item_copy[i] += 1
                list_item_copy.sort(reverse = True)
                new_tuple = tuple( list_item_copy )
                if new_tuple in digit_pattern_tuples[ index_num_digits ]:
                    digit_pattern_combos[new_tuple] += digit_pattern_combos[tuple_item] 
                if new_tuple not in digit_pattern_tuples[ index_num_digits ] and new_tuple[0] <=3:
                    digit_pattern_tuples[ index_num_digits ].append( new_tuple )
                    digit_pattern_combos[new_tuple] = digit_pattern_combos[tuple_item] 


    # print len(digit_pattern_combos)
    # print digit_pattern_combos.keys()
    
    total_combos = 0
    for k, v in digit_pattern_combos.items():
        if sum(k) == limit_num_digits:
            total_combos += v

    return total_combos

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 172 solution is:",  e172()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
