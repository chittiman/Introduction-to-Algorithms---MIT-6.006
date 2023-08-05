# test_static_array.py

import pytest
from static_array import StaticArray

class TestStaticArrayLen:
    def test_empty_array(self):
        arr = StaticArray(0)
        assert len(arr) == 0

    def test_non_empty_array(self):
        arr = StaticArray(5)
        assert len(arr) == 5

class TestStaticArrayGetItem:
    def test_get_valid_index(self):
        arr = StaticArray(5)
        arr[0] = 10
        assert arr[0] == 10

    def test_get_invalid_index_raises_exception(self):
        arr = StaticArray(3)
        with pytest.raises(Exception, match='Index is out of range'):
            arr[5]

class TestStaticArraySetItem:
    def test_set_valid_index(self):
        arr = StaticArray(3)
        arr[1] = 20
        assert arr[1] == 20

    def test_set_invalid_index_raises_exception(self):
        arr = StaticArray(2)
        with pytest.raises(Exception, match='Index is out of range'):
            arr[3] = 30

class TestStaticArrayRepr:
    def test_repr_empty_array(self):
        arr = StaticArray(0)
        assert repr(arr) == '[]'

    def test_repr_non_empty_array(self):
        arr = StaticArray(3)
        arr[0] = 1
        arr[1] = 2
        arr[2] = 3
        assert repr(arr) == '[1, 2, 3]'

class TestStaticArrayIter:
    def test_iter_empty_array(self):
        arr = StaticArray(0)
        assert list(arr) == []

    def test_iter_non_empty_array(self):
        arr = StaticArray(4)
        arr[0] = 'a'
        arr[3] = 'd'
        assert list(arr) == ['a', None, None, 'd']

