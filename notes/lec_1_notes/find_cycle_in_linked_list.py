# Recitation 2 - Problem 1

def find_cycle_length(ll_head):
    slow_pointer = ll_head.later_node(1)
    fast_pointer = ll_head.later_node(2)
    
    #Move till both meet
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.later_node(1)
        fast_pointer = fast_pointer.later_node(2)
    
    meet_node = slow_pointer
    slow_pointer = slow_pointer.later_node(1)
    i = 1
    while meet_node != slow_pointer:
        slow_pointer = slow_pointer.later_node(1)
        i += 1
    return i

    #Once both are met move fast_pointer to start
    # and move till meet

    


