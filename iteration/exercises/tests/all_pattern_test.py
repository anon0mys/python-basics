import pytest


class AllPatternTest:
    def test_1(self):
        account_balances = [0, 0, 0, 0, 0, 0, 0]
        all_zeros = True
        for balance in account_balances:
            if not balance == 0:
                all_zeros = False

        assert all_zeros is True

    def test_2(self):
        account_balances = {
          "checking": 0,
          "saving": 0,
          "retirement_401k": 0,
          "retirement_ira": 0,
        }
        all_zeros = True
        for balance in account_balances.values():
            if not balance == 0:
                all_zeros = False

        assert all_zeros is True

    @pytest.mark.skip
    def test_3(self):
        words = ["love", "hate", "fire", "bird", "call"]
        all_four_letters = False
        # Your Code Here

        assert all_four_letters is True

    @pytest.mark.skip
    def test_4(self):
        words = {
          "one": "love",
          "two": "hate",
          "three": "fire",
          "four": "bird",
          "five": "call"
        }
        all_four_letters = False
        # Your Code Here

        assert all_four_letters is True

    @pytest.mark.skip
    def test_5(self):
        statuses = ["busy", "busy", "busy"]
        all_busy = False
        # Your Code Here

        assert all_busy is True

    @pytest.mark.skip
    def test_6(self):
        friend_status = {
          "Megan": "busy",
          "Sarah": "busy",
          "Duncan": "busy",
        }
        all_busy = False
        # Your Code Here

        assert all_busy is True

    @pytest.mark.skip
    def test_7(self):
        zip_codes = [94381, 831, 50009, 36232, 8992, 89999, 11110]
        # Your Code Here
        all_five_digits = None

        assert all_five_digits is False

    @pytest.mark.skip
    def test_8(self):
        zip_codes = {
          "Megan": 94381,
          "Sarah": 831,
          "Duncan": 50009,
          "Raymart": 36232,
          "Alec": 89092,
          "Cameron": 89999,
          "Joshua": 11110
        }
        # Your Code Here
        all_five_digits = None

        assert all_five_digits is False

    @pytest.mark.skip
    def test_9(self):
        snacks = ["GARLIC PLANTAINS", "SNICKERDOODLES", "Pretzels"]
        # Your Code Here
        all_caps = None

        assert all_caps is False

    @pytest.mark.skip
    def test_10(self):
        snacks = {
          "savory": "GARLIC PLANTAINS",
          "sweet": "SNICKERDOODLES",
          "salty": "Pretzels"
        }
        # Your Code Here
        all_caps = None

        assert all_caps is False
