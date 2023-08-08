# test_dynamic_array.py

import pytest
from dynamic_array import DynamicArray

class TestDynamicArrayInsertAt:
    def test_insert_at_empty_array(self):
        arr = DynamicArray(0)
        arr.insert_at(0, 'value')
        assert len(arr) == 1
        assert arr[0] == 'value'

    def test_insert_at_beginning(self):
        arr = DynamicArray(3)
        arr[1] = 'b'
        arr[2] = 'c'
        arr.insert_at(0, 'a')
        assert len(arr) == 4
        assert arr[0] == 'a'
        assert arr[1] == None
        assert arr[2] == 'b'
        assert arr[3] == 'c'

    def test_insert_at_end(self):
        arr = DynamicArray(3)
        arr[0] = 'a'
        arr[1] = 'b'
        arr.insert_at(3, 'c')
        assert len(arr) == 4
        assert arr[0] == 'a'
        assert arr[1] == 'b'
        assert arr[2] == None
        assert arr[3] == 'c'

    def test_insert_at_middle(self):
        arr = DynamicArray(4)
        arr[0] = 'a'
        arr[1] = 'c'
        arr[2] = 'd'
        arr.insert_at(1, 'b')
        assert len(arr) == 5
        assert arr[1] == 'b'
        assert arr[2] == 'c'

    def test_insert_at_invalid_index_raises_exception(self):
        arr = DynamicArray(2)
        with pytest.raises(Exception, match='Index is out of range'):
            arr.insert_at(3, 'b')
    
class TestDynamicArrayDeleteAt:
    def test_delete_at_empty_array(self):
        arr = DynamicArray(0)
        with pytest.raises(Exception, match='Index is out of range'):
            arr.delete_at(0)

    def test_delete_one_element_array(self):
        arr = DynamicArray(1)
        arr[0] = 'a'
        item = arr.delete_at(0)
        assert len(arr) == 0
        assert item == 'a'
        
    def test_delete_at_beginning(self):
        arr = DynamicArray(3)
        arr[0] = 'a'
        arr[1] = 'b'
        arr[2] = 'c'
        item = arr.delete_at(0)
        assert item == 'a'
        assert len(arr) == 2
        assert arr[0] == 'b'
        assert arr[1] == 'c'

    def test_delete_at_end(self):
        arr = DynamicArray(3)
        arr[0] = 'a'
        arr[1] = 'b'
        arr[2] = 'c'
        item = arr.delete_at(2)
        assert item == 'c'
        assert len(arr) == 2
        assert arr[0] == 'a'
        assert arr[1] == 'b'

    def test_delete_at_middle(self):
        arr = DynamicArray(4)
        arr[0] = 'a'
        arr[1] = 'b'
        arr[2] = 'c'
        arr[3] = 'd'
        item = arr.delete_at(1)
        assert item == 'b'
        assert len(arr) == 3
        assert arr[0] == 'a'
        assert arr[1] == 'c'

class TestDynamicArrayInsertFirst:
    def test_insert_first_empty_array(self):
        arr = DynamicArray(0)
        arr.insert_first('value')
        assert len(arr) == 1
        assert arr[0] == 'value'

    def test_insert_first_existing_array(self):
        arr = DynamicArray(3)
        arr[0] = 'b'
        arr[1] = 'c'
        arr.insert_first('a')
        assert len(arr) == 4
        assert arr[0] == 'a'
        assert arr[1] == 'b'

class TestDynamicArrayDeleteFirst:
    def test_delete_first_empty_array(self):
        arr = DynamicArray(0)
        with pytest.raises(Exception, match='Index is out of range'):
            arr.delete_first()

    def test_delete_first_existing_array(self):
        arr = DynamicArray(3)
        arr[0] = 'a'
        arr[1] = 'b'
        arr[2] = 'c'
        deleted_item = arr.delete_first()
        assert len(arr) == 2
        assert deleted_item == 'a'
        assert arr[0] == 'b'

class TestDynamicArrayInsertLast:
    def test_insert_last_empty_array(self):
        arr = DynamicArray(0)
        arr.insert_last('value')
        assert len(arr) == 1
        assert arr[0] == 'value'

    def test_insert_last_existing_array(self):
        arr = DynamicArray(3)
        arr[1] = 'a'
        arr[2] = 'b'
        arr.insert_last('c')
        assert len(arr) == 4
        assert arr[2] == 'b'
        assert arr[3] == 'c'

class TestDynamicArrayDeleteLast:
    def test_delete_last_empty_array(self):
        arr = DynamicArray(0)
        with pytest.raises(Exception, match='Index is out of range'):
            arr.delete_last()

    def test_delete_last_existing_array(self):
        arr = DynamicArray(3)
        arr[0] = 'a'
        arr[1] = 'b'
        arr[2] = 'c'
        deleted_item = arr.delete_last()
        assert len(arr) == 2
        assert deleted_item == 'c'
        assert arr[1] == 'b'



