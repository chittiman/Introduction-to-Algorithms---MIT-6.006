# test_linked_list_node.py

import pytest
from linked_list import LinkedList,LinkedListNode
import re

class TestLinkedListNodeInit:
    def test_initialization(self):
        node = LinkedListNode(10)
        assert node.item == 10
        assert node.next is None

class TestLinkedListNodeLaterNode:
    def test_later_node_zero(self):
        node = LinkedListNode(5)
        later = node.later_node(0)
        assert later.item == 5

    def test_later_node_positive(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node1.next = node2
        node2.next = node3

        later = node1.later_node(2)
        assert later.item == 3

    def test_later_node_out_of_range(self):
        node = LinkedListNode(7)
        error_msg = f'Later Node is None for {node}'
        with pytest.raises(Exception, match=re.escape(error_msg)):
            node.later_node(2)

    def test_later_node_next_none(self):
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node1.next = node2
        error_msg = f'Later Node is None for {node2}'
        with pytest.raises(Exception, match=re.escape(error_msg)):
            node1.later_node(2)

class TestLinkedListNodeRepr:
    def test_repr(self):
        node = LinkedListNode(42)
        node_repr = repr(node)
        assert "item = 42" in node_repr

class TestLinkedListInit:
    def test_initialization(self):
        linked_list = LinkedList()
        assert linked_list.head is None
        assert len(linked_list) == 0

class TestLinkedListBuild:
    def test_build_empty_list(self):
        linked_list = LinkedList()
        linked_list.build([])
        assert linked_list.head is None
        assert len(linked_list) == 0

    def test_build_non_empty_list(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        assert len(linked_list) == 3

        current_node = linked_list.head
        assert current_node.item == 1
        assert current_node.next.item == 2
        assert current_node.next.next.item == 3
        assert current_node.next.next.next is None

class TestLinkedListLen:
    def test_len_empty_list(self):
        linked_list = LinkedList()
        assert len(linked_list) == 0

    def test_len_non_empty_list(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        assert len(linked_list) == 3

class TestLinkedListIter:
    def test_iter_empty_list(self):
        linked_list = LinkedList()
        items = list(linked_list)
        assert items == []

    def test_iter_non_empty_list(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        items = list(linked_list)
        assert items == [1, 2, 3]

class TestLinkedListGetItem:
    def test_getitem_empty_list(self):
        linked_list = LinkedList()
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list[0]

    def test_getitem_valid_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3, 4, 5])
        assert linked_list[2] == 3

    def test_getitem_invalid_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list[5]

    def test_getitem_negative_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list[-1]

class TestLinkedListSetItem:
    def test_setitem_empty_list(self):
        linked_list = LinkedList()
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list[0] = 10

    def test_setitem_valid_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3, 4, 5])
        linked_list[2] = 7
        assert linked_list[2] == 7

    def test_setitem_invalid_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list[5] = 8

    def test_setitem_negative_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list[-1] = 9

class TestLinkedListInsertFirst:
    def test_insert_first_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert_first(10)
        assert len(linked_list) == 1
        assert linked_list[0] == 10
        assert linked_list.head.item == 10

    def test_insert_first_existing_list(self):
        linked_list = LinkedList()
        linked_list.build([2, 3])
        linked_list.insert_first(1)
        assert len(linked_list) == 3
        assert linked_list[0] == 1
        assert linked_list[1] == 2
        assert linked_list[2] == 3
        assert linked_list.head.item == 1
        assert linked_list.head.next.item == 2
                   
class TestLinkedListDeleteFirst:
    def test_delete_first_empty_list(self):
        linked_list = LinkedList()
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list.delete_first()

    def test_delete_first_single_item_list(self):
        linked_list = LinkedList()
        linked_list.build([42])
        deleted_item = linked_list.delete_first()
        assert len(linked_list) == 0
        assert deleted_item == 42
        assert linked_list.head is None

    def test_delete_first_existing_list(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        deleted_item = linked_list.delete_first()
        assert len(linked_list) == 2
        assert deleted_item == 1
        assert linked_list.head.item == 2
        assert linked_list[0] == 2

class TestLinkedListInsertAt:
    def test_insert_at_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert_at(0, 10)
        assert len(linked_list) == 1
        assert linked_list.head.item == 10
        assert linked_list[0] == 10

    def test_insert_at_beginning(self):
        linked_list = LinkedList()
        linked_list.build([2, 3])
        linked_list.insert_at(0, 1)
        assert len(linked_list) == 3
        assert linked_list.head.item == 1
        assert linked_list.head.next.item == 2
        assert linked_list[0] == 1
        assert linked_list[1] == 2

    def test_insert_at_middle(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 4])
        linked_list.insert_at(2, 3)
        assert len(linked_list) == 4
        assert linked_list.head.next.next.item == 3
        assert linked_list.head.next.next.next.item == 4
        assert linked_list[1] == 2
        assert linked_list[2] == 3
        assert linked_list[3] == 4

    def test_insert_at_end(self):
        linked_list = LinkedList()
        linked_list.build([1, 2])
        linked_list.insert_at(2, 3)
        assert len(linked_list) == 3
        assert linked_list.head.next.next.item == 3
        assert linked_list[1] == 2
        assert linked_list[2] == 3

    def test_insert_at_invalid_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list.insert_at(5, 4)

class TestLinkedListDeleteAt:
    def test_delete_at_empty_list(self):
        linked_list = LinkedList()
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list.delete_at(0)

    def test_delete_at_beginning(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        deleted_item = linked_list.delete_at(0)
        assert len(linked_list) == 2
        assert deleted_item == 1
        assert linked_list.head.item == 2

    def test_delete_at_middle(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        deleted_item = linked_list.delete_at(1)
        assert len(linked_list) == 2
        assert deleted_item == 2
        assert linked_list.head.next.item == 3

    def test_delete_at_end(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        deleted_item = linked_list.delete_at(2)
        assert len(linked_list) == 2
        assert deleted_item == 3
        assert linked_list.head.next.next is None

    def test_delete_at_invalid_index(self):
        linked_list = LinkedList()
        linked_list.build([1, 2, 3])
        with pytest.raises(Exception, match='Index is out of range'):
            linked_list.delete_at(5)

