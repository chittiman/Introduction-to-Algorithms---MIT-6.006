# test_binary_search.py

from binary_search import binary_search

class TestBinarySearch:
    def test_empty_array(self):
        A = []
        index = binary_search(A, 5)
        assert index is None

    def test_item_exists(self):
        A = [1, 3, 5, 7, 9]
        index = binary_search(A, 5)
        assert index == 2

    def test_item_does_not_exist(self):
        A = [1, 3, 5, 7, 9]
        index = binary_search(A, 4)
        assert index is None

    def test_item_at_start(self):
        A = [1, 3, 5, 7, 9]
        index = binary_search(A, 1)
        assert index == 0

    def test_item_at_end(self):
        A = [1, 3, 5, 7, 9]
        index = binary_search(A, 9)
        assert index == 4

    def test_item_at_middle(self):
        A = [1, 3, 5, 7, 9]
        index = binary_search(A, 5)
        assert index == 2

    def test_item_at_middle_with_duplicates(self):
        A = [1, 3, 5, 5, 7, 9]
        index = binary_search(A, 5)
        assert index == 2

    def test_item_range(self):
        A = [1, 3, 5, 7, 9]
        index = binary_search(A, 5, start=1, end=4)
        assert index == 2

    def test_repetition_at_start(self):
        A = [3, 3, 5, 7, 9]
        index = binary_search(A, 3)
        assert index == 0

    def test_repetition_at_end(self):
        A = [1, 3, 5, 7, 7]
        index = binary_search(A, 7)
        assert index == 3

    def test_repetition_at_middle(self):
        A = [1, 3, 3, 5, 7, 9]
        index = binary_search(A, 3)
        assert index == 1

    # Add more tests as needed

