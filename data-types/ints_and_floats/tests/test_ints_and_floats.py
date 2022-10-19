import pytest


class IntsAndFloatsTest:
    def test_one(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # add the lucky number and the unlucky number
        sum = None
        assert sum == 20

    @pytest.mark.skip
    def test_two(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # subtract the unlucky from the lucky
        difference = None
        assert difference == -6

    @pytest.mark.skip
    def test_three(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # divide unlucky by lucky
        # NOTE: this is integer division
        quotient = None
        assert quotient == 1

    @pytest.mark.skip
    def test_four(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # divide unlucky by lucky
        quotient = None
        assert quotient == 1.8571428571428572

    @pytest.mark.skip
    def test_five(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # find the remainder of the unlucky divided by the lucky
        remainder = None
        assert remainder == 6

    @pytest.mark.skip
    def test_six(self):
        lucky = 7
        # Using the variable defined above,
        # find out if the lucky number is even
        even = None
        assert even == False

    @pytest.mark.skip
    def test_seven(self):
        pi = 3.14
        # Using the variable defined above,
        # round the number to the nearest whole number
        rounded = None
        assert rounded == 3

    @pytest.mark.skip
    def test_eight(self):
        pi = 3.14
        # Using the variable defined above,
        # round the number to one decimal place
        rounded = None
        assert rounded == 3.1

    @pytest.mark.skip
    def test_nine(self):
        pi = 3.14
        # Using the variable defined above,
        # round the number to the next highest whole number
        rounded = None
        assert rounded == 4
