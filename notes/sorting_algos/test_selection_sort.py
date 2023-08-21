from selection_sort import selection_sort,find_arg_max_prefix

class TestSelectionSort:
    def test_empty_array(self):
        A = []
        selection_sort(A)
        assert A == []

    def test_sorted_array(self):
        A = [1, 2, 3, 4, 5]
        selection_sort(A)
        assert A == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        A = [5, 4, 3, 2, 1]
        selection_sort(A)
        assert A == [1, 2, 3, 4, 5]

    def test_mixed_array(self):
        A = [3, 1, 4, 2, 5]
        selection_sort(A)
        assert A == [1, 2, 3, 4, 5]

    def test_duplicate_values(self):
        A = [3, 1, 4, 2, 5, 3]
        selection_sort(A)
        assert A == [1, 2, 3, 3, 4, 5]

    def test_partial_sort(self):
        A = [5, 4, 3, 2, 1]
        selection_sort(A, 3)
        assert A == [2, 3, 4, 5, 1]

    # Add more tests as needed



class TestFindArgMaxPrefix:
    def test_single_element(self):
        A = [5]
        assert find_arg_max_prefix(A, 0) == 0

    def test_sorted_array(self):
        A = [1, 2, 3, 4, 5]
        assert find_arg_max_prefix(A, 4) == 4

    def test_reverse_sorted_array(self):
        A = [5, 4, 3, 2, 1]
        assert find_arg_max_prefix(A, 4) == 0

    def test_mixed_array(self):
        A = [3, 1, 4, 2, 5]
        assert find_arg_max_prefix(A, 4) == 4

    def test_duplicate_values(self):
        A = [3, 1, 4, 2, 5, 3]
        assert find_arg_max_prefix(A, 5) == 4

    def test_partial_sort(self):
        A = [5, 4, 3, 2, 1]
        assert find_arg_max_prefix(A, 2) == 0

    def test_partial_sort_with_duplicates(self):
        A = [5, 4, 3, 2, 1, 5]
        assert find_arg_max_prefix(A, 4) == 0

# Add more tests as needed

