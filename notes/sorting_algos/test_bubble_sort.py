# test_bubble_sort.py

from bubble_sort import bubble_sort, swap_round

class TestBubbleSort:
    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_sorted_list(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_list(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_mixed_list(self):
        assert bubble_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]

    def test_duplicate_values(self):
        assert bubble_sort([3, 1, 4, 2, 5, 3]) == [1, 2, 3, 3, 4, 5]


class TestSwapRound:
    def test_no_swaps(self):
        A = [1, 2, 3, 4, 5]
        swap_count = swap_round(A, 4)
        assert A == [1, 2, 3, 4, 5]
        assert swap_count == 0

    def test_swaps_needed(self):
        A = [3, 1, 4, 2, 5]
        swap_count = swap_round(A, 4)
        assert A == [1, 3, 2, 4, 5]
        assert swap_count == 2

    def test_all_swaps(self):
        A = [5, 4, 3, 2, 1]
        swap_count = swap_round(A, 4)
        assert A == [4, 3, 2, 1, 5]
        assert swap_count == 4

    def test_swaps_for_two_elements(self):
        A = [2, 1]
        swap_count = swap_round(A, 1)
        assert A == [1, 2]
        assert swap_count == 1

    def test_no_swaps_for_two_elements(self):
        A = [1, 2]
        swap_count = swap_round(A, 1)
        assert A == [1, 2]
        assert swap_count == 0

    def test_partial_swaps(self):
        A = [5, 2, 3, 4, 1]
        swap_count = swap_round(A, 3)
        assert A == [2, 3, 4, 5, 1]
        assert swap_count == 3

# Add more tests as needed

