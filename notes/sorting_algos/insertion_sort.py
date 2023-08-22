def insertion_sort(A,a=None):
    a = 1 if a is None else a
    if len(A) > 1 and a < len(A): 
        'sorted_array = A[:a] next element is A[a]'
        next_element = A[a]
        i = a 
        while i>=1 and A[i] < A[i-1]:
            A[i],A[i-1] = A[i-1],A[i]
            i -= 1
        a += 1
        return insertion_sort(A,a)
    else:
        return A
    