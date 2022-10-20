import pytest


class MapPatternTest:
    def test_1(self):
        names = ["alice", "bob", "charlie"]
        capitalized_names = []
        for name in names:
          capitalized_names.append(name.capitalize())

        assert capitalized_names == ["Alice", "Bob", "Charlie"]

    @pytest.mark.skip
    def test_2(self):
        family = {
          "mother": "alice",
          "father": "bob",
          "brother": "charlie"
        }
        capitalized_family = {}
        for relationship, name in family.items():
            capitalized_family[relationship] = name.capitalize

        expected = {
          "mother": "Alice",
          "father": "Bob",
          "brother": "Charlie"
        }
        assert capitalized_family == expected

    @pytest.mark.skip
    def test_3(self):
        numbers = [1, 2, 3, 4, 5]
        doubles = []
        # Your Code Here

        assert doubles == [2, 4, 6, 8, 10]

    @pytest.mark.skip
    def test_4(self):
        numbers = {
          "one": 1,
          "two": 2,
          "three": 3,
          "four": 4,
          "five": 5
        }
        doubles = {}
        # Your Code Here

        expected = {
          "one": 2,
          "two": 4,
          "three": 6,
          "four": 8,
          "five": 10
        }
        assert doubles == expected

    @pytest.mark.skip
    def test_5(self):
        numbers = [1, 2, 3, 4, 5]
        squares = []
        # Your Code Here

        assert squares == [1, 4, 9, 16, 25]

    @pytest.mark.skip
    def test_6(self):
        numbers = {
          "one": 1,
          "two": 2,
          "three": 3,
          "four": 4,
          "five": 5
        }
        squares = {}
        # Your Code Here

        expected = {
          "one": 1,
          "two": 4,
          "three": 9,
          "four": 16,
          "five": 25
        }
        assert squares == expected

    @pytest.mark.skip
    def test_7(self):
        names = ["alice", "bob", "charlie", "david", "eve"]
        #Your Code Here
        lengths = None

        assert lengths == [5, 3, 7, 5, 3]

    @pytest.mark.skip
    def test_8(self):
        family = {
          "mother": "alice",
          "father": "bob",
          "brother": "charlie",
          "uncle": "david",
          "sister": "eve"
        }
        #Your Code Here
        lengths = None

        expected = {
          "mother": 5,
          "father": 3,
          "brother": 7,
          "uncle": 5,
          "sister": 3
        }
        assert lengths == expected

    @pytest.mark.skip
    def test_9(self):
        names = ["alice", "bob", "charlie", "david", "eve"]
        #Your Code Here
        backwards = None

        assert backwards == ["ecila", "bob", "eilrahc", "divad", "eve"]

    @pytest.mark.skip
    def test_10(self):
        family = {
          "mother": "alice",
          "father": "bob",
          "brother": "charlie",
          "uncle": "david",
          "sister": "eve"
        }
        #Your Code Here
        backwards = None

        expected = {
          "mother": "ecila",
          "father": "bob",
          "brother": "eilrahc",
          "uncle": "divad",
          "sister": "eve"
        }
        assert backwards == expected
