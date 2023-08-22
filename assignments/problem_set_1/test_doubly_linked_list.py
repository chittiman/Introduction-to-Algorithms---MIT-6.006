from doubly_Linked_List_Seq import Doubly_Linked_List_Node,Doubly_Linked_List_Seq
import pytest 

class TestDoublyLinkedListNodeInit:
    def test_init(self):
        value = 42
        node = Doubly_Linked_List_Node(value)
        assert node.item == value
        assert node.prev is None
        assert node.next is None

class TestDoublyLinkedListNodeLaterNode:
    def test_later_node_base_case(self):
        node = Doubly_Linked_List_Node(1)
        result = node.later_node(0)
        assert result.item == 1

    def test_later_node_recursive_case(self):
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        node3 = Doubly_Linked_List_Node(3)
        node1.next = node2
        node2.next = node3
        node2.prev = node1
        node3.prev = node2

        result = node1.later_node(2)
        assert result.item == 3

    def test_later_node_out_of_bounds(self):
        node = Doubly_Linked_List_Node(1)
        with pytest.raises(AssertionError):
            node.later_node(1)

class TestDoublyLinkedListSeqLaterNode:
    def test_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_add_to_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node = Doubly_Linked_List_Node(42)
        linked_list.head = linked_list.tail = node
        assert linked_list.head == node
        assert linked_list.tail == node
        assert node.prev is None
        assert node.next is None

    def test_add_to_non_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        linked_list.head = node1
        linked_list.tail = node2
        node1.next = node2
        node2.prev = node1

        assert linked_list.head == node1
        assert linked_list.tail == node2
        assert node1.prev is None
        assert node1.next == node2
        assert node2.prev == node1
        assert node2.next is None

class TestDoublyLinkedListSeqIter:
    def test_iter_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        result = list(linked_list)
        assert result == []

    def test_iter_non_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        linked_list.head = node1
        linked_list.tail = node2
        node1.next = node2
        node2.prev = node1

        result = list(linked_list)
        assert result == [1, 2]

class TestDoublyLinkedListSeqStr:
    def test_str_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        result = str(linked_list)
        assert result == ''

    def test_str_non_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        linked_list.head = node1
        linked_list.tail = node2
        node1.next = node2
        node2.prev = node1

        result = str(linked_list)
        assert result == '(1)-(2)'

class TestDoublyLinkedListSeqGetAt:
    def test_get_at_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        with pytest.raises(AttributeError):
            linked_list.get_at(0)

    def test_get_at_single_item_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node = Doubly_Linked_List_Node(42)
        linked_list.head = linked_list.tail = node
        result = linked_list.get_at(0)
        assert result == 42

    def test_get_at_multiple_items_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        linked_list.head = node1
        linked_list.tail = node2
        node1.next = node2
        node2.prev = node1

        result = linked_list.get_at(1)
        assert result == 2

class TestDoublyLinkedListSeqSetAt:
    def test_set_at_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        with pytest.raises(AttributeError):
            linked_list.set_at(0, 42)

    def test_set_at_single_item_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node = Doubly_Linked_List_Node(0)
        linked_list.head = linked_list.tail = node
        linked_list.set_at(0, 42)
        assert node.item == 42

    def test_set_at_multiple_items_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        linked_list.head = node1
        linked_list.tail = node2
        node1.next = node2
        node2.prev = node1

        linked_list.set_at(1, 99)
        assert node2.item == 99

class TestDoublyLinkedListSeqInsertFirst:
    def test_insert_first_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.insert_first(42)
        assert linked_list.head.item == 42
        assert linked_list.tail.item == 42
        assert linked_list.head.prev is None
        assert linked_list.head.next is None

    def test_insert_first_non_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        linked_list.head = linked_list.tail = node1

        linked_list.insert_first(99)
        assert linked_list.head.item == 99
        assert linked_list.tail.item == 1
        assert linked_list.head.prev is None
        assert linked_list.head.next == node1
        assert node1.prev == linked_list.head

    def test_insert_first_multiple_elements(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        node3 = Doubly_Linked_List_Node(3)
        linked_list.head = node1
        linked_list.tail = node3
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2

        linked_list.insert_first(99)
        assert linked_list.head.item == 99
        assert linked_list.tail.item == 3
        assert linked_list.head.prev is None
        assert linked_list.head.next == node1
        assert node1.prev == linked_list.head
        assert node1.next == node2
        assert node2.prev == node1
        assert node2.next == node3
        assert node3.prev == node2

class TestDoublyLinkedListSeqInsertLast:
    def test_insert_last_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.insert_last(42)
        assert linked_list.head.item == 42
        assert linked_list.tail.item == 42
        assert linked_list.head.prev is None
        assert linked_list.head.next is None

    def test_insert_last_non_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        linked_list.head = linked_list.tail = node1

        linked_list.insert_last(99)
        assert linked_list.head.item == 1
        assert linked_list.tail.item == 99
        assert linked_list.tail.prev == node1
        assert linked_list.tail.next is None
        assert node1.next == linked_list.tail

    def test_insert_last_multiple_elements(self):
        linked_list = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(1)
        node2 = Doubly_Linked_List_Node(2)
        node3 = Doubly_Linked_List_Node(3)
        linked_list.head = node1
        linked_list.tail = node3
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2

        linked_list.insert_last(99)
        assert linked_list.head.item == 1
        assert linked_list.tail.item == 99
        assert linked_list.tail.prev == node3
        assert linked_list.tail.next is None
        assert node3.next == linked_list.tail

class TestDoublyLinkedListSeqBuild:
    def test_build_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([])
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_build_single_element_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([42])
        assert linked_list.head.item == 42
        assert linked_list.tail.item == 42
        assert linked_list.head.prev is None
        assert linked_list.head.next is None

    def test_build_multiple_elements(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4])
        assert linked_list.head.item == 1
        assert linked_list.tail.item == 4

        current_node = linked_list.head
        for i in range(1, 5):
            assert current_node.item == i
            if i < 4:
                assert current_node.next.item == i + 1
                assert current_node.next.prev == current_node
                current_node = current_node.next

class TestDoublyLinkedListSeqDeleteFirst:
    def test_delete_first_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        result = linked_list.delete_first()
        assert result is None
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_first_single_element_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([42])
        result = linked_list.delete_first()
        assert result == 42
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_first_two_element_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([42, 99])
        result = linked_list.delete_first()
        assert result == 42
        assert linked_list.head.item == 99
        assert linked_list.tail.item == 99
        assert linked_list.head.prev is None
        assert linked_list.head.next is None

    def test_delete_first_multiple_elements(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4])
        result = linked_list.delete_first()
        assert result == 1
        assert linked_list.head.item == 2
        assert linked_list.tail.item == 4
        assert linked_list.head.prev is None
        assert linked_list.head.next.item == 3

class TestDoublyLinkedListSeqDeleteLast:
    def test_delete_last_empty_list(self):
        linked_list = Doubly_Linked_List_Seq()
        result = linked_list.delete_last()
        assert result is None
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_last_single_element_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([42])
        result = linked_list.delete_last()
        assert result == 42
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_last_multiple_elements(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4])
        result = linked_list.delete_last()
        assert result == 4
        assert linked_list.head.item == 1
        assert linked_list.tail.item == 3

    def test_delete_last_two_element_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([42, 99])
        result = linked_list.delete_last()
        assert result == 99
        assert linked_list.head.item == 42
        assert linked_list.tail.item == 42
        assert linked_list.head.prev is None
        assert linked_list.head.next is None

class TestDoublyLinkedListSeqRemove:
    def test_remove_from_middle(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4, 5])
        
        node2 = linked_list.head.next
        node4 = node2.next.next
        removed_list = linked_list.remove(node2, node4)

        ##ll = [1,5]

        assert linked_list.head.item == 1
        assert linked_list.tail.item == 5
        assert linked_list.head.next.item == 5
        assert linked_list.tail.prev.item == 1

        ## rem_list = [2,3,4]
        assert removed_list.head.item == 2
        assert removed_list.tail.item == 4
        assert removed_list.head.prev is None
        assert removed_list.tail.next is None

    def test_remove_from_start(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4, 5])
        
        node1 = linked_list.head
        node3 = node1.next.next
        removed_list = linked_list.remove(node1, node3)

        ##ll = [4,5]

        assert linked_list.head.item == 4
        assert linked_list.tail.item == 5
        assert linked_list.head.prev is None
        assert linked_list.head.next.item == 5
        assert linked_list.tail.prev.item == 4

        assert removed_list.head.item == 1
        assert removed_list.tail.item == 3
        assert removed_list.head.prev is None
        assert removed_list.tail.next is None

    def test_remove_from_end(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4, 5])
        
        node4 = linked_list.tail.prev
        removed_list = linked_list.remove(node4, linked_list.tail)

        ##ll = [1,2,3]

        assert linked_list.head.item == 1
        assert linked_list.tail.item == 3
        assert linked_list.tail.next is None
        assert linked_list.tail.prev.item == 2

        assert removed_list.head.item == 4
        assert removed_list.tail.item == 5
        assert removed_list.head.prev is None
        assert removed_list.tail.next is None

    def test_remove_entire_list(self):
        linked_list = Doubly_Linked_List_Seq()
        linked_list.build([1, 2, 3, 4, 5])
        
        removed_list = linked_list.remove(linked_list.head, linked_list.tail)

        assert linked_list.head is None
        assert linked_list.tail is None

        assert removed_list.head.item == 1
        assert removed_list.tail.item == 5
        assert removed_list.head.prev is None
        assert removed_list.tail.next is None

class TestDoublyLinkedListSeqSplice:

    def test_splice_into_middle(self):
        linked_list1 = Doubly_Linked_List_Seq()
        linked_list1.build([1, 2, 3])

        linked_list2 = Doubly_Linked_List_Seq()
        linked_list2.build([4, 5])

        node2 = linked_list1.head.next
        linked_list1.splice(node2, linked_list2)

        assert list(linked_list1) == [1,2,4,5,3]

        assert linked_list2.head is None
        assert linked_list2.tail is None

    def test_splice_into_start(self):
        linked_list1 = Doubly_Linked_List_Seq()
        linked_list1.build([1, 2, 3])

        linked_list2 = Doubly_Linked_List_Seq()
        linked_list2.build([4, 5])

        node1 = linked_list1.head
        linked_list1.splice(node1, linked_list2)

        assert list(linked_list1) == [1,4,5,2,3]

        assert linked_list2.head is None
        assert linked_list2.tail is None

    def test_splice_into_end(self):
        linked_list1 = Doubly_Linked_List_Seq()
        linked_list1.build([1, 2, 3])

        linked_list2 = Doubly_Linked_List_Seq()
        linked_list2.build([4, 5])

        node3 = linked_list1.tail
        linked_list1.splice(node3, linked_list2)

        assert list(linked_list1) == [1,2,3,4,5]

        assert linked_list2.head is None
        assert linked_list2.tail is None

    def test_splice_empty_list_into_middle(self):
        linked_list1 = Doubly_Linked_List_Seq()
        linked_list1.build([1, 2, 3])

        linked_list2 = Doubly_Linked_List_Seq()  # Empty list
        node2 = linked_list1.head.next
        linked_list1.splice(node2, linked_list2)

        assert linked_list1.head.item == 1
        assert linked_list1.tail.item == 3
        assert linked_list1.head.next.item == 2
        assert linked_list1.head.next.next.item == 3
        assert linked_list1.head.next.next.next is None

        assert linked_list2.head is None
        assert linked_list2.tail is None

    def test_splice_empty_list_into_start(self):
        linked_list1 = Doubly_Linked_List_Seq()
        linked_list1.build([1, 2, 3])

        linked_list2 = Doubly_Linked_List_Seq()  # Empty list
        node1 = linked_list1.head
        linked_list1.splice(node1, linked_list2)

        assert linked_list1.head.item == 1
        assert linked_list1.tail.item == 3
        assert linked_list1.head.next.item == 2
        assert linked_list1.head.next.next.item == 3
        assert linked_list1.head.next.next.next is None

        assert linked_list2.head is None
        assert linked_list2.tail is None

    def test_splice_empty_list_into_end(self):
        linked_list1 = Doubly_Linked_List_Seq()
        linked_list1.build([1, 2, 3])

        linked_list2 = Doubly_Linked_List_Seq()  # Empty list
        node3 = linked_list1.tail
        linked_list1.splice(node3, linked_list2)

        assert linked_list1.head.item == 1
        assert linked_list1.tail.item == 3
        assert linked_list1.head.next.item == 2
        assert linked_list1.head.next.next.item == 3
        assert linked_list1.head.next.next.next is None

        assert linked_list2.head is None
        assert linked_list2.tail is None




