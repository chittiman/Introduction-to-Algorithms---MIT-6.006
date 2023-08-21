def bubble_sort(A):
    end = len(A) -1
    swap_counter = -1
    while swap_counter != 0:
        swap_counter = swap_round(A,end)
        end -= 1
    return A

def swap_round(A,end):
    swap_counter = 0
    for i in range(end):
        if A[i] <= A[i+1]:
            pass
        else:
            A[i],A[i+1] = A[i+1],A[i]
            swap_counter += 1
    return swap_counter


if __name__ == '__main__':
    A = [5,6,21,5,66,83,23,0]
    print(bubble_sort(A))