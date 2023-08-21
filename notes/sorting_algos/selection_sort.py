def selection_sort(A,i=None):
    if i is None:
        i = len(A)-1
    if i > 0:
        max_index = find_arg_max_prefix(A,i-1)
        if A[i] >= A[max_index]:
            pass
        else:
            A[i],A[max_index] = A[max_index],A[i]
        selection_sort(A,i-1)
    else:
        pass

def find_arg_max_prefix(A,i):
    'Return index of max value in A[:i+1]'
    if i > 0:
        prev_max_index = find_arg_max_prefix(A,i-1)
        if A[i] >= A[prev_max_index]:
            return i
        else:
            return prev_max_index
    else:
        return 0