import pytest


class FindPatternTest:
    def test_1(self):
        ages = [39, 45, 29, 24, 50]
        younger_than_thirty = None
        for age in ages:
            if age < 30:
                younger_than_thirty = age
                break

        assert younger_than_thirty == 29

    def test_2(self):
        ages = {
            "abdi": 39,
            "hassan": 45,
            "ladonna": 29,
            "margaret": 24,
            "miguel": 50
        }
        younger_than_thirty = None
        for name in ages:
            if ages[name] < 30:
                younger_than_thirty = name
                break

        assert younger_than_thirty == "ladonna"

    @pytest.mark.skip
    def test_3(self):
        ages = [39, 45, 29, 24, 50]
        older_than_fifty = None
        for age in ages:
            # Your Code Here
            pass

        assert older_than_fifty is None

    @pytest.mark.skip
    def test_4(self):
        ages = {
            "abdi": 39,
            "hassan": 45,
            "ladonna": 29,
            "margaret": 24,
            "miguel": 50
        }
        older_than_fifty = None
        for name in ages:
            # your code here
            pass

        assert older_than_fifty is None

    @pytest.mark.skip
    def test_5(self):
        ages = [39, 45, 29, 24, 50]
        multiple_of_three = None
        # Your Code Here

        assert multiple_of_three == 39

    @pytest.mark.skip
    def test_6(self):
        ages = {
            "abdi": 39,
            "hassan": 45,
            "ladonna": 29,
            "margaret": 24,
            "miguel": 50
        }
        multiple_of_three = None
        # Your Code Here

        assert multiple_of_three == "abdi"

    @pytest.mark.skip
    def test_7(self):
        people = ["Willie", "Carmen Sandiego", "Bryan", "Faith", "Zac"]
        # Your Code Here
        carmen = None

        assert carmen == "Carmen Sandiego"

    @pytest.mark.skip
    def test_8(self):
        places = {
            "Bangkok": "Willie",
            "Santa Fe": "Carmen Sandiego",
            "Rome": "Bryan",
            "Munich": "Faith",
            "Mogudishu": "Zac"
        }
        # Your Code Here
        where_is_carmen_sandiego = None

        assert where_is_carmen_sandiego == "Santa Fe"

    @pytest.mark.skip
    def test_9(self):
        numbers = [3, 7, 13, 11, 10, 2, 17]
        # Your Code Here
        even = None

        assert even == 10

    @pytest.mark.skip
    def test_10(self):
        purchases = {
            "shoes": "paid",
            "backpack": "paid",
            "books": "pending",
            "posters": "paid",
            "food": "pending"
        }
        # Your Code Here
        pending = None

        assert pending == "books"

    @pytest.mark.skip
    def test_11(self):
        purchases = {
            "shoes": "paid",
            "backpack": "paid",
            "books": "pending",
            "posters": "paid",
            "food": "pending"
        }
        # Your Code Here
        starts_with_b = None

        assert starts_with_b == "backpack"
