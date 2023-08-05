from count_long_subarray import count_long_subarray,update_count_max_len

class TestCountLongSubarray:
    def test_one(self):
        array = (2, 2, 4, 1, 4)
        actual = 2
        predicted = count_long_subarray(array)
        assert actual == predicted

    def test_two(self):
        array = (7, 8, 5, 7, 7, 3, 2, 8)
        actual = 3
        predicted = count_long_subarray(array)
        assert actual == predicted

    def test_three(self):
        array = (7, 7, 9, 1, 2, 11, 9, 6, 2, 8, 9)
        actual = 2
        predicted = count_long_subarray(array)
        assert actual == predicted

    def test_four(self):
        array = (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3)
        actual = 1
        predicted = count_long_subarray(array)
        assert actual == predicted

    def test_five(self):
        array = (11, 16, 10, 19, 20, 18, 3, 19, 2, 1, 8, 17, 7, 13, 1, 11, 1, 18, 19, 9, 7, 19, 24, 2, 12)
        actual = 4
        predicted = count_long_subarray(array)
        assert actual == predicted

class TestUpdateCountMaxLen:

    def test_update_count_max_len_when_pres_len_greater_than_max_len(self):
        max_len, count = update_count_max_len(10, 5, 0)
        assert max_len == 10
        assert count == 1

    def test_update_count_max_len_when_pres_len_equals_max_len(self):
        max_len, count = update_count_max_len(7, 7, 3)
        assert max_len == 7
        assert count == 4

    def test_update_count_max_len_when_pres_len_less_than_max_len(self):
        max_len, count = update_count_max_len(3, 6, 8)
        assert max_len == 6
        assert count == 8


    # def test_six(self):
    #     array = (9,8,7,6,5,4,3,2,1)
    #     actual = 9
    #     predicted = count_long_subarray(array)
    #     assert actual == predicted