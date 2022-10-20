import pytest


class MaxAndMinPatternTest:
    def test_1(self):
        numbers = [1, 100, 1000, 1000000]
        greatest = numbers[0]
        for number in numbers:
            if number > greatest:
                greatest = number

        assert greatest == 1000000

    @pytest.mark.skip
    def test_2(self):
        magnitudes = {
            "ones": 1,
            "hundreds": 100,
            "thousands": 1000,
            "millions": 1000000
        }
        greatest = magnitudes["ones"]
        for key in magnitudes:
            if magnitudes[key] > greatest:
                greatest = magnitudes[key]

        assert greatest == 1000000

    @pytest.mark.skip
    def test_3(self):
        meals = ["banana", "nuts", "salad", "steak", "cake"]
        shortest_word = meals[0]
        # Your Code Here

        assert shortest_word == "nuts"

    @pytest.mark.skip
    def test_4(self):
        meals = {
            "breakfast": "banana",
            "snack": "nuts",
            "lunch": "salad",
            "dinner": "steak",
            "dessert": "cake"
        }
        shortest_word = meals["breakfast"]
        # Your Code Here

        assert shortest_word == "nuts"

    @pytest.mark.skip
    def test_5(self):
        stats = [3001, 431, 1695, 0.27601, 0.340]
        most_digits = stats[0]
        # Your Code Here

        assert most_digits == 0.27601

    @pytest.mark.skip
    def test_6(self):
        stats = {
            "games_played": 3001,
            "home_runs": 431,
            "rbi": 1695,
            "batting_average": 0.27601,
            "on_base_percentage": 0.340
        }
        most_digits = stats["games_played"]
        # Your Code Here

        assert most_digits == 0.27601

    @pytest.mark.skip
    def test_7(self):
        ages = [39, 45, 29, 24, 50]
        # Your Code Here
        oldest = None

        assert oldest == 50

    @pytest.mark.skip
    def test_8(self):
        ages = {
            "abdi": 39,
            "hassan": 45,
            "ladonna": 29,
            "margaret": 24,
            "miguel": 50
        }
        # Your Code Here
        oldest = None

        expected = {"name": "miguel", "age": 50}
        assert oldest == expected

    @pytest.mark.skip
    def test_9(self):
        programmers = [["katrina", "sandi", "jim", "aaron", "desi"], ["abby", "jon", "susan"]]
        # Your Code Here
        fewest_programmers = None

        assert fewest_programmers == ["abby", "jon", "susan"]

    @pytest.mark.skip
    def test_10(self):
        programmers = {"ruby": ["katrina", "sandi", "jim", "aaron", "desi"], "java": ["abby", "jon", "susan"]}
        # Your Code Here
        fewest_programmers = None

        assert fewest_programmers == "java"
