def merge_sort(A):
    if len(A) >1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        L = merge_sort(L)
        R = merge_sort(R)
        return merge(L,R)
    else:
        return A

def merge(L,R,M=None,i=None,j=None,k=None):
    M = [None]*(len(L)+len(R)) if M is None else M
    i = len(L)-1  if i is None else i
    j = len(R)-1  if j is None else j
    k = len(M)-1  if k is None else k
    if k >=0: 
        if i >= 0 and j >=0:
            if L[i] > R[j]:
                M[k] = L[i]
                i -= 1
            else:
                M[k] = R[j]
                j -= 1
        elif i <0:
            M[k] = R[j]
            j -= 1
        elif j <0:
            M[k] = L[i]
            i -= 1
        k -= 1
        return merge(L,R,M,i,j,k)
    else:
        return M

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    sorted_A = merge_sort(A)
    assert sorted_A == [1, 2, 3, 4, 5]

    




    


