# test_merge.py

from merge_sort import merge, merge_sort

class TestMergeSort:
    def test_empty_array(self):
        A = []
        sorted_A = merge_sort(A)
        assert sorted_A == []

    def test_single_element_array(self):
        A = [1]
        sorted_A = merge_sort(A)
        assert sorted_A == [1]

    def test_sorted_array(self):
        A = [1, 2, 3, 4, 5]
        sorted_A = merge_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        A = [5, 4, 3, 2, 1]
        sorted_A = merge_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_mixed_array(self):
        A = [3, 1, 4, 2, 5]
        sorted_A = merge_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_duplicate_values(self):
        A = [3, 1, 4, 2, 5, 3]
        sorted_A = merge_sort(A)
        assert sorted_A == [1, 2, 3, 3, 4, 5]

    def test_partial_sort(self):
        A = [1, 2, 3, 5, 4]
        sorted_A = merge_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_partial_sort_with_duplicates(self):
        A = [5, 4, 3, 2, 1, 5]
        sorted_A = merge_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5, 5]

    # Add more tests as needed



class TestMerge:
    def test_merge_empty_arrays(self):
        L = []
        R = []
        merged = merge(L, R)
        assert merged == []

    def test_merge_left_empty(self):
        L = []
        R = [3, 5, 7]
        merged = merge(L, R)
        assert merged == [3, 5, 7]

    def test_merge_right_empty(self):
        L = [1, 4, 6]
        R = []
        merged = merge(L, R)
        assert merged == [1, 4, 6]

    def test_merge_equal_lengths(self):
        L = [1, 3, 5]
        R = [2, 4, 6]
        merged = merge(L, R)
        assert merged == [1, 2, 3, 4, 5, 6]

    def test_merge_unequal_lengths(self):
        L = [1, 3]
        R = [2, 4, 6]
        merged = merge(L, R)
        assert merged == [1, 2, 3, 4, 6]
    
    

    # Add more tests as needed

