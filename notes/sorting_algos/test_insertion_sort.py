from insertion_sort import insertion_sort
class TestInsertionSort:
    def test_empty_array(self):
        A = []
        sorted_A = insertion_sort(A)
        assert sorted_A == []

    def test_single_element_array(self):
        A = [1]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1]

    def test_sorted_array(self):
        A = [1, 2, 3, 4, 5]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        A = [5, 4, 3, 2, 1]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_mixed_array(self):
        A = [3, 1, 4, 2, 5]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_duplicate_values(self):
        A = [3, 1, 4, 2, 5, 3]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1, 2, 3, 3, 4, 5]

    def test_partial_sort(self):
        A = [1, 2, 3, 5, 4]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5]

    def test_partial_sort_with_duplicates(self):
        A = [5, 4, 3, 2, 1, 5]
        sorted_A = insertion_sort(A)
        assert sorted_A == [1, 2, 3, 4, 5, 5]