from linked_list import LinkedList

def reverse_linked_list(L):
    if L.size <= 1:
        return L,L.head
    else:
        node = remove_first_node(L)
        L,tail = reverse_linked_list(L)
        L,tail = add_last_node(L,tail,node)
        return L,tail
        
def remove_first_node(L):
    if L.size == 0:
        return None
    else:
        first_node = L.head
        L.size -= 1
        L.head = first_node.next
    return first_node

def add_last_node(L,tail,node):
    node.next = None
    tail.next = node
    L.size += 1
    return L,node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.build([1,2,3,4,5])
    out,_ = reverse_linked_list(linked_list)
    print(list(out))
