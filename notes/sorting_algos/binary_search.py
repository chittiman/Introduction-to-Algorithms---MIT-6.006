def binary_search(A,k,start=0,end=None):
    '''
    Given a sorted array A and an item k,find in A[start:end]
     - index i if item's first occurence
    '''
    end = len(A) if end is None else end
    if end > start:
        mid = (start+end)//2
        if A[mid] == k:
            if mid > start and A[mid-1]==k:
                return binary_search(A,k,start,mid)
            else:
                return mid
        elif A[mid] > k:
            return binary_search(A,k,start,mid)
        elif A[mid] < k:
            return binary_search(A,k,mid+1,end)
    else:
        return None
