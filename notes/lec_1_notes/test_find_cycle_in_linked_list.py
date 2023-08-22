import pytest
from linked_list import LinkedList, LinkedListNode
from find_cycle_in_linked_list import find_cycle_length  # Import your module here

# Test Case 2: Cycle with Even Length
def test_cycle_even_length():
    linked_list = LinkedList()
    linked_list.build([1, 2, 3, 4, 5])
    node_5 = linked_list.head.later_node(4)
    node_3 = linked_list.head.later_node(2)
    node_5.next = node_3
    num_nodes_in_cycle = find_cycle_length(linked_list.head)
    assert num_nodes_in_cycle == 3

# Test Case 3: Cycle with Odd Length
def test_cycle_odd_length():
    linked_list = LinkedList()
    linked_list.build([1, 2, 3, 4, 5, 6])
    node_6 = linked_list.head.later_node(5)
    node_3 = linked_list.head.later_node(2)
    node_6.next = node_3
    num_nodes_in_cycle = find_cycle_length(linked_list.head)
    assert num_nodes_in_cycle == 4

# Test Case 4: Single Element Cycle
def test_single_element_cycle():
    linked_list = LinkedList()
    linked_list.build([1, 2, 3])
    node_3 = linked_list.head.later_node(2)
    node_3.next = node_3
    num_nodes_in_cycle = find_cycle_length(linked_list.head)
    assert num_nodes_in_cycle == 1

# Test Case 5: End Connected to Head (Circular Linked List)
def test_circular_linked_list():
    linked_list = LinkedList()
    linked_list.build([1, 2, 3, 4, 5])
    last_node = linked_list.head.later_node(4)
    last_node.next = linked_list.head
    num_nodes_in_cycle = find_cycle_length(linked_list.head)
    assert num_nodes_in_cycle == 5

# Test Case 6: End Connected to a Middle Node (Non-Circular Linked List)
def test_non_circular_linked_list():
    linked_list = LinkedList()
    linked_list.build([1, 2, 3, 4, 5])
    node_2 = linked_list.head.later_node(1)
    last_node = linked_list.head.later_node(4)
    last_node.next = node_2
    num_nodes_in_cycle = find_cycle_length(linked_list.head)
    assert num_nodes_in_cycle == 4
