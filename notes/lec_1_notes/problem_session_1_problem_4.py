from linked_list import LinkedList
from reverse_linked_list import reverse_linked_list

def reorder_students(L):
    '''
    Input: L
    | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
    - any additional linked list nodes
    - any other non-constant-sized data structures
    '''
    ##################
    # YOUR CODE HERE #

    head_node = L.head
    size = L.size # = 2n
    n = size //2
    first_half_final_node = head_node.later_node(n-1) #first_halh -0 -> n-1
    second_half = LinkedList()
    second_half.head = first_half_final_node.next
    second_half.size = n
    reverse_second_half,_ = reverse_linked_list(second_half)
    first_half_final_node.next = reverse_second_half.head
    ##################
    return L



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.build(range(1,3))
    a = reorder_students(linked_list)
    print(list(a))
    #print(list(reverse_linked_list(linked_list)[0]))
    # print(list(linked_list))
    # node = remove_first_node(linked_list)
    # node.next = None
    # print(node)
    # print(list(linked_list))


    #print(list(reorder_students(linked_list)))
