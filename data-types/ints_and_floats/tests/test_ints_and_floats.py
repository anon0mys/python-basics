import pytest
import math

class IntsAndFloatsTest:
    def test_one(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # add the lucky number and the unlucky number
        sum = lucky + unlucky
        assert sum == 20

    def test_two(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # subtract the unlucky from the lucky
        difference = lucky - unlucky
        assert difference == -6

    def test_three(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # divide unlucky by lucky
        # NOTE: this is integer division
        quotient = unlucky//lucky
        assert quotient == 1

    def test_four(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # divide unlucky by lucky
        quotient = unlucky/lucky
        assert quotient == 1.8571428571428572

    def test_five(self):
        lucky = 7
        unlucky = 13
        # Using the two variables defined above,
        # find the remainder of the unlucky divided by the lucky
        remainder = unlucky%lucky
        assert remainder == 6

    def test_six(self):
        lucky = 7
        # Using the variable defined above,
        # find out if the lucky number is even
        even = ""
        if (7 % 2) == 0:
            return even == True
            assert even == False

    def test_seven(self):
        pi = 3.14
        # Using the variable defined above,
        # round the number to the nearest whole number
        rounded = round(pi)
        assert rounded == 3

    def test_eight(self):
        pi = 3.14
        # Using the variable defined above,
        # round the number to one decimal place
        rounded = round(pi, 1)
        assert rounded == 3.1

    def test_nine(self):
        pi = 3.14
        # Using the variable defined above,
        # round the number to the next highest whole number
        rounded = math.ceil(3.14)
        assert rounded == 4
