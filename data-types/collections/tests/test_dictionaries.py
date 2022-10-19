import pytest


class DictionariesTest:
    def test_one(self):
        # In the line below, create a new empty hash called empty
        empty = None
        assert empty == {}

    @pytest.mark.skip
    def test_two(self):
        # In the line below, create an empty hash with a default value 0
        empty = {}
        assert empty['not_found'] == 0

    @pytest.mark.skip
    def test_three(self):
        # In the line below, create a hash called ages. The hash should
        # have a key of "ben" with a value of 4 and a key of "kelly" with
        # a value of 6
        ages = {}
        assert len(ages) == 2
        assert ages["ben"] == 4
        assert ages["kelly"] == 6

    @pytest.mark.skip
    def test_four(self):
        # In the line below, create a new hash with
        # default values of zero
        # create a "tomatoes" key and a 1 key
        ingredients = {}

        assert ingredients["tomatoes"] == 0
        assert ingredients[1] == 0

    @pytest.mark.skip
    def test_five(self):
        books = {
            "John Steinbeck": "Grapes of Wrath",
            "Harper Lee": "To Kill a Mockingbird"
        }
        # Using the books hash defined above,
        # access the value "Grapes of Wrath"  in the line below
        grapes = None
        assert grapes == "Grapes of Wrath"

    @pytest.mark.skip
    def test_six(self):
        books = {
            "John Steinbeck": "Grapes of Wrath",
            "Harper Lee": "To Kill a Mockingbird"
        }
        # Using the books hash defined above,
        # add a new key of "Ernest Hemmingway"
        # with a value of "For Whom the Bell Tolls"
        # in the line below

        expected = {
            "John Steinbeck": "Grapes of Wrath",
            "Harper Lee": "To Kill a Mockingbird",
            "Ernest Hemmingway": "For Whom the Bell Tolls"
        }
        assert books == expected

    @pytest.mark.skip
    def test_seven(self):
        books = {
            "John Steinbeck": "Grapes of Wrath",
            "Harper Lee": "To Kill a Mockingbird"
        }
        # Using the books hash defined above,
        # change the value associated with
        # "John Steinbeck" to "Of Mice and Men"

        expected = {
            "John Steinbeck": "Of Mice and Men",
            "Harper Lee": "To Kill a Mockingbird"
        }
        assert books == expected

    @pytest.mark.skip
    def test_eight(self):
        books = {
            "John Steinbeck": "Grapes of Wrath",
            "Harper Lee": "To Kill a Mockingbird"
        }
        # Using the books hash defined above,
        # delete the key "Harper Lee"

        expected = {
            "John Steinbeck": "Grapes of Wrath"
        }
        assert books == expected

    @pytest.mark.skip
    def test_nine(self):
        ages = {
            "Jimmy": 4,
            "Julio": 8,
            "Juliet": 9
        }
        # Using the ages hash defined above
        # increment Julio's age by one

        assert ages["Julio"] == 9

    @pytest.mark.skip
    def test_ten(self):
        ages = {
            "Jimmy": 4,
            "Julio": 8,
            "Juliet": 9
        }
        # Using the ages hash defined above
        # get an array of all the ages
        age_list = None
        assert age_list == [4, 8, 9]

    @pytest.mark.skip
    def test_eleven(self):
        ages = {
            "Jimmy": 4,
            "Julio": 8,
            "Juliet": 9
        }
        # Using the ages hash defined above
        # find the number of key/value pairs
        num_pairs = None
        assert num_pairs == 3

    @pytest.mark.skip
    def test_twelve(self):
        ages = {
            "Jimmy": 4,
            "Julio": 8,
            "Juliet": 9
        }
        # Call a method on the ages hash defined above
        # to figure out if :Jimmy is a key
        jimmy_in_hash = None
        assert jimmy_in_hash is True

        # Now figure out if :Jackie is in the hash

        jackie_in_hash = None
        assert jackie_in_hash is False
