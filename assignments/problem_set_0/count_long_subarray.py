def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    ##################
    # YOUR CODE HERE #
    count = 1
    max_len = 1
    
    pres_len = 1
    prev = A[0]

    for i,pres in enumerate(A[1:],start=1):
        if pres > prev :
            pres_len += 1
            if pres_len > max_len:
                max_len = pres_len
                count = 1
            elif pres_len == max_len:
                count += 1
            else:
                pass
        else:
            pres_len = 1
        prev = pres

    ##################
    return count

if __name__ == "__main__":
    array = (2, 2, 4, 1, 4)
    print (count_long_subarray(array))