import pytest


class SelectPatternTest:
    def test_1(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        evens = []
        for number in numbers:
            if number % 2 == 0:
                evens.append(number)

        assert evens == [2, 4, 6, 8, 10]

    def test_2(self):
        numbers = {
          "one": 1,
          "two": 2,
          "three": 3,
          "four": 4,
          "five": 5,
        }
        evens = {}
        for name in numbers:
          if numbers[name] % 2 == 0:
            evens[name] = numbers[name]

        expected = {
          "two": 2,
          "four": 4
        }
        assert evens == expected

    @pytest.mark.skip
    def test_3(self):
        rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        greater_than_four = []
        #Your Code Here

        assert greater_than_four == ["orange", "yellow", "green", "indigo", "violet"]

    @pytest.mark.skip
    def test_4(self):
        rainbow = {
          "first": "red",
          "second": "orange",
          "third": "yellow",
          "fourth": "green",
          "fifth": "blue",
          "sixth": "indigo",
          "seventh": "violet"
        }
        greater_than_four = {}
        #Your Code Here


        expected = {
          "second": "orange",
          "third": "yellow",
          "fourth": "green",
          "sixth": "indigo",
          "seventh": "violet"
        }
        assert greater_than_four == expected

    @pytest.mark.skip
    def test_5(self):
        furniture = ["dining table", "bed", "coffee table", "deck chairs"]
        words_with_c = []
        #Your Code Here

        assert words_with_c == ["coffee table", "deck chairs"]

    @pytest.mark.skip
    def test_6(self):
        furniture = {
          "dining_room": "dining table",
          "bedroom": "bed",
          "living_room": "coffee table",
          "patio": "deck chairs"
        }
        words_with_c = {}
        #Your Code Here

        expected = {
          "living_room": "coffee table",
          "patio": "deck chairs"
        }
        assert words_with_c == expected

    @pytest.mark.skip
    def test_7(self):
        meals = ["chips and salsa", "chicken alfredo", "banana pudding"]
        #Your Code Here
        two_words = None

        assert two_words == ["chicken alfredo", "banana pudding"]

    @pytest.mark.skip
    def test_8(self):
        meal = {
          "appetizer": "chips and salsa",
          "entre": "chicken alfredo",
          "dessert": "banana pudding"
        }
        #Your Code Here
        two_words = None

        expected = {
          "entre": "chicken alfredo",
          "dessert": "banana pudding"
        }
        assert two_words == expected


    @pytest.mark.skip
    def test_9(self):
        prices = [3, 1.4, 3.5, 2, 4.9, 9.1, 8.0]
        #Your Code Here
        floats = None

        assert floats == [1.4, 3.5, 4.9, 9.1, 8.0]

    @pytest.mark.skip
    def test_10(self):
        items = {
          "tv": 3,
          "toaster": 1.4,
          "basketball": 3.5,
          "bucket": 2,
          "lint_roller": 4.9,
          "sack_o_potatoes": 9.1,
          "tonka_truck": 8.0
        }
        #Your Code Here
        floats = None

        expected = {
          "toaster": 1.4,
          "basketball": 3.5,
          "lint_roller": 4.9,
          "sack_o_potatoes": 9.1,
          "tonka_truck": 8.0
        }
        assert floats == expected
