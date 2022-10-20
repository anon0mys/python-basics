from collections import defaultdict

import pytest


class GroupByPatternTest:
    def by_word_length(self):
        words = ["sue", "alice", "steve", "sally", "adam", "fort", "tops", "dog", "cat"]
        grouped = defaultdict(list)
        for word in words:
            grouped[len(word)].append(word)

        expected = {
            3: ["sue", "dog", "cat"],
            4: ["adam", "fort", "tops"],
            5: ["alice", "steve", "sally"]
        }
        assert grouped == expected

    @pytest.mark.skip
    def by_odd_and_even(self):
        numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        odd_and_even = defaultdict(list)
        for number in numbers:
            pass

        expected = {1: [1, 1, 3, 5, 13, 21, 55], 0: [2, 8, 34]}
        assert odd_and_even == expected

    @pytest.mark.skip
    def by_first_letter(self):
        words = ["ant", "axis", "albatross", "bolt", "badge", "butter", "car", "cdr", "column"]
        words_by_first_letter = defaultdict(list)
        # Your code goes here
        expected = {
            "a": ["ant", "axis", "albatross"],
            "b": ["bolt", "badge", "butter"],
            "c": ["car", "cdr", "column"]
        }
        assert words_by_first_letter == expected

    @pytest.mark.skip
    def by_uniqueness(self):
        words = ["one", "two", "one", "TWO", "three", "one", "three", "three", "three"]
        # Your code goes here
        grouped = None
        expected = {
            "one": ["one", "one", "one"],
            "two": ["two", "TWO"],
            "three": ["three", "three", "three", "three"]
        }
        assert grouped == expected

    @pytest.mark.skip
    def by_number_of_zeroes(self):
        numbers = [1, 3, 500, 200, 4000, 3000, 10000, 90, 20, 500000]
        # Your code goes here
        grouped = None
        expected = {0: [1, 3], 2: [500, 200], 3: [4000, 3000], 4: [10000], 1: [90, 20], 5: [500000]}
        assert grouped == expected

    @pytest.mark.skip
    def by_order_of_magnitude(self):
        numbers = [1, 3, 503, 239, 4938, 3932, 19982, 93, 21, 501787]
        # Your code goes here
        grouped = None
        expected = {1: [1, 3], 2: [93, 21], 3: [503, 239], 4: [4938, 3932], 5: [19982], 6: [501787]}
        assert grouped == expected
