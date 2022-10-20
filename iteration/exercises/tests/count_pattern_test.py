import pytest


class CountPatternTest:
    def test_1(self):
        ages = [39, 45, 29, 24, 50]
        younger_than_thirty = 0
        for age in ages:
            if age < 30:
                younger_than_thirty += 1

        assert younger_than_thirty == 2

    @pytest.mark.skip
    def test_2(self):
        ages = {
          "abdi": 39,
          "hassan": 45,
          "ladonna": 29,
          "margaret": 24,
          "miguel": 50
        }
        younger_than_thirty = 0
        for name in ages:
            if ages[name] < 30:
                younger_than_thirty += 1

        assert younger_than_thirty == 2

    @pytest.mark.skip
    def test_3(self):
        ages = [39, 45, 29, 24, 50]
        older_than_fifty = 0
        for age in ages:
            pass
            # Your Code Here

        assert older_than_fifty == 0

    @pytest.mark.skip
    def test_4(self):
        ages = {
          "abdi": 39,
          "hassan": 45,
          "ladonna": 29,
          "margaret": 24,
          "miguel": 50
        }
        older_than_fifty = 0
        # Your Code Here

        assert older_than_fifty == 0

    @pytest.mark.skip
    def test_5(self):
        ages = [39, 45, 29, 24, 50]
        multiple_of_three = 0
        # Your Code Here

        assert multiple_of_three == 3

    @pytest.mark.skip
    def test_6(self):
        ages = {
          "abdi": 39,
          "hassan": 45,
          "ladonna": 29,
          "margaret": 24,
          "miguel": 50
        }
        multiple_of_three = 0
        # Your Code Here

        assert multiple_of_three == 3

    @pytest.mark.skip
    def test_7(self):
        family = ["alice", "bob", "charlie", "david", "eve"]
        # Your Code Here
        names_with_three_letters = None

        assert names_with_three_letters == 2

    @pytest.mark.skip
    def test_8(self):
        family = {
          "mother": "alice",
          "father": "bob",
          "brother": "charlie",
          "uncle": "david",
          "sister": "eve"
        }
        # Your Code Here
        names_with_three_letters = None

        assert names_with_three_letters == 2

    @pytest.mark.skip
    def test_9(self):
        prices = [1.0, 3.9, 5.99, 18.5, 20.0]
        # Your code goes here
        whole_numbers = None

        assert whole_numbers == 2

    @pytest.mark.skip
    def test_10(self):
        prices = {
          "shoes": 1.0,
          "backpack": 3.9,
          "books": 5.99,
          "posters": 18.5,
          "food": 20.0
        }
        # Your Code Here
        whole_numbers = None

        assert whole_numbers == 2
