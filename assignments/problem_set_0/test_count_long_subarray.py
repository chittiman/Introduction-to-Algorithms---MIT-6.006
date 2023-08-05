from count_long_subarray import count_long_subarray

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
    
    # def test_six(self):
    #     array = (9,8,7,6,5,4,3,2,1)
    #     actual = 9
    #     predicted = count_long_subarray(array)
    #     assert actual == predicted