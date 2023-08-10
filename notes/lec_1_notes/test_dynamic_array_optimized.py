# test_dynamic_array_seq.py

import pytest
from dynamic_array_optimized import DynamicArraySeq

class TestDynamicArraySeqInit:
    def test_initialization_default_ratio(self):
        dynamic_array = DynamicArraySeq()
        assert dynamic_array.size == 0
        assert dynamic_array.ratio == 2
        assert len(dynamic_array.data) == 2
        assert dynamic_array.space == 2
        assert dynamic_array.lower_bound == 1 / (2 * 2)
        assert dynamic_array.upper_bound == 2

    def test_initialization_custom_ratio(self):
        dynamic_array = DynamicArraySeq(ratio=3)
        assert dynamic_array.ratio == 3
        assert len(dynamic_array.data) == 3
        assert dynamic_array.lower_bound == 1 / (3 * 3)
        assert dynamic_array.upper_bound == 3

class TestDynamicArraySeqLen:
    def test_len_empty_array(self):
        dynamic_array = DynamicArraySeq()
        assert len(dynamic_array) == 0

    def test_len_non_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.size = 3
        assert len(dynamic_array) == 3

class TestDynamicArraySeqIter:
    def test_iter_empty_array(self):
        dynamic_array = DynamicArraySeq()
        items = list(dynamic_array)
        assert items == []

    def test_iter_non_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.size = 3
        dynamic_array.data = [1, 2, 3]
        items = list(dynamic_array)
        assert items == [1, 2, 3]

class TestDynamicArraySeqInsertLast:
    def test_insert_last_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.insert_last(10)
        assert len(dynamic_array) == 1
        assert dynamic_array.data[0] == 10
        assert dynamic_array.space == 2

    def test_insert_last_non_empty_array_no_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.size = 3
        dynamic_array.data = [1, 2, 3,None]
        dynamic_array.space = 4
        dynamic_array.insert_last(4)
        assert len(dynamic_array) == 4
        assert list(dynamic_array) == [1, 2, 3, 4]
        assert dynamic_array.space == 4

    def test_insert_last_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.size = 4
        dynamic_array.data = [1, 2, 3, 4]
        dynamic_array.space = 4
        dynamic_array.insert_last(5)
        assert len(dynamic_array) == 5
        assert list(dynamic_array) == [1, 2, 3, 4, 5]
        assert dynamic_array.space == 8

class TestDynamicArraySeqBuild:
    def test_build_empty_sequence(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([])
        assert len(dynamic_array) == 0
        assert list(dynamic_array) == []
        assert dynamic_array.space == 2

    def test_build_non_empty_sequence_no_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1, 2])
        assert len(dynamic_array) == 2
        assert list(dynamic_array) == [1, 2]
        assert dynamic_array.space == 2

    def test_build_non_empty_sequence_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1, 2, 3])
        assert len(dynamic_array) == 3
        assert list(dynamic_array) == [1, 2, 3]
        assert dynamic_array.space == 4

class TestDynamicArraySeqInsertAt:
    def test_insert_at_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.insert_at(0, 10)
        assert len(dynamic_array) == 1
        assert dynamic_array.data[0] == 10
        assert dynamic_array.space == 2

    def test_insert_at_non_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1,3,4])
        dynamic_array.insert_at(1, 2)
        assert len(dynamic_array) == 4
        assert list(dynamic_array) == [1, 2, 3,4]
        assert dynamic_array.space == 4

    def test_insert_at_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1, 2, 3, 5])
        dynamic_array.insert_at(3, 4)
        assert len(dynamic_array) == 5
        assert list(dynamic_array) == [1, 2, 3, 4, 5]
        assert dynamic_array.space == 8

class TestDynamicArraySeqInsertFirst:
    def test_insert_first_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.insert_first(10)
        assert len(dynamic_array) == 1
        assert list(dynamic_array) == [10]
        assert dynamic_array.space == 2

    def test_insert_first_non_empty_array_no_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1,2,3])
        dynamic_array.insert_first(0)
        assert len(dynamic_array) == 4
        assert list(dynamic_array) == [0,1, 2, 3]
        assert dynamic_array.space == 4

    def test_insert_first_non_empty_array_resizing(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1,2,3,4])
        dynamic_array.insert_first(0)
        assert len(dynamic_array) == 5
        assert list(dynamic_array) == [0,1, 2, 3,4]
        assert dynamic_array.space == 8

class TestDynamicArraySeqDeleteLast:
    def test_delete_last_empty_array(self):
        dynamic_array = DynamicArraySeq()
        with pytest.raises(Exception, match='Index is out of range'):
            dynamic_array.delete_last()

    def test_delete_last_non_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1, 2, 3])
        deleted_item = dynamic_array.delete_last()
        assert len(dynamic_array) == 2
        assert deleted_item == 3

    # Add tests for resizing

class TestDynamicArraySeqDeleteAt:
    def test_delete_at_empty_array(self):
        dynamic_array = DynamicArraySeq()
        with pytest.raises(Exception, match='Index is out of range'):
            dynamic_array.delete_at(0)

    def test_delete_at_non_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1, 2, 3])
        deleted_item = dynamic_array.delete_at(1)
        assert len(dynamic_array) == 2
        assert deleted_item == 2

    # Add tests for resizing

class TestDynamicArraySeqDeleteFirst:
    def test_delete_first_empty_array(self):
        dynamic_array = DynamicArraySeq()
        with pytest.raises(Exception, match='Index is out of range'):
            dynamic_array.delete_first()

    def test_delete_first_non_empty_array(self):
        dynamic_array = DynamicArraySeq()
        dynamic_array.build([1, 2, 3])
        deleted_item = dynamic_array.delete_first()
        assert len(dynamic_array) == 2
        assert deleted_item == 1

    # Add tests for resizing

# class TestDynamicArraySeqDeleteLast:
#     def test_delete_last_resize_down(self):
#         dynamic_array = DynamicArraySeq()
#         dynamic_array.build([1, 2, 3, 4, 5, 6])
#         dynamic_array.delete_last()
#         dynamic_array.delete_last()
#         assert len(dynamic_array) == 4
#         assert dynamic_array.data == [1, 2, 3, 4]
#         assert dynamic_array.space == 8

#     # Add more resize down tests

# class TestDynamicArraySeqDeleteAt:
#     def test_delete_at_resize_down(self):
#         dynamic_array = DynamicArraySeq()
#         dynamic_array.build([1, 2, 3, 4, 5, 6])
#         dynamic_array.delete_at(2)
#         dynamic_array.delete_at(2)
#         assert len(dynamic_array) == 4
#         assert dynamic_array.data == [1, 2, 5, 6]
#         assert dynamic_array.space == 8

#     # Add more resize down tests

# class TestDynamicArraySeqDeleteFirst:
#     def test_delete_first_resize_down(self):
#         dynamic_array = DynamicArraySeq()
#         dynamic_array.build([1, 2, 3, 4, 5, 6])
#         dynamic_array.delete_first()
#         dynamic_array.delete_first()
#         assert len(dynamic_array) == 4
#         assert dynamic_array.data == [3, 4, 5, 6]
#         assert dynamic_array.space == 8

# Add more test classes and test cases for other methods



