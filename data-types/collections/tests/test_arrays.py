import pytest


class ArraysTest:
    def test_one(self):
        # in the line below, create a new empty array
        empty = None
        assert empty == []

    @pytest.mark.skip
    def test_two(self):
        # in the line below, create an array with the numbers 1 through 5
        nums = None

        assert nums == [1,2,3,4,5]

    @pytest.mark.skip
    def test_three(self):
        # in the line below, access the second element
        nums = [1, 2, 3]
        actual = None

        expected = 2
        assert actual == expected

    @pytest.mark.skip
    def test_four(self):
        # In the line below, call a method on the nums variable
        # defined above to access the last element
        nums = [1, 2, 3]
        actual = None
        expected = 3
        assert actual == expected

        # Now try to find another way to achieve the same effect
        nums = [1, 2, 3]
        actual = None
        expected = 3
        assert actual == expected

    @pytest.mark.skip
    def test_five(self):
        hummus = ["tahini", "chickpeas", "lemons"]
        # Use a function that will tell us how many elements there are in the hummus array
        actual = None
        assert actual == 3

    @pytest.mark.skip
    def test_six(self):
        world_cup = ["Germany", "Mexico", "Iceland", "Portugal"]
        # In the line below, add the element "Brazil" to the end of the world_cup array

        assert world_cup[-1] == "Brazil"

        # Use a different method to add the element "Japan" to the end of the array

        assert world_cup[-1] == "Japan"

    @pytest.mark.skip
    def test_seven(self):
        world_cup = ["Germany", "Mexico", "Iceland", "Portugal"]
        # Call a method on the world_cup variable to remove and return
        # the last element of the array
        last_element = None
        assert last_element == "Portugal"
        assert world_cup == ["Germany", "Mexico", "Iceland"]

    @pytest.mark.skip
    def test_eight(self):
        karaoke = ["Shake it Off", "Dancing Queen", "Bohemian Rhapsody"]
        # Call a method on the karaoke variable to ask whether "Toxic"
        # is an element or not
        toxic_in_array = None
        assert toxic_in_array == False

        # Now call a method on the karaoke variable to ask whether "Dancing Queen"
        # is an element or not
        dancing_queen_in_array = None
        assert dancing_queen_in_array == True

    @pytest.mark.skip
    def test_nine(self):
        band = ["Guitar", "Drums", "Bass"]
        # Call a method on the band variable to add the element "Vocals"
        # to the beginning of the array

        assert band == ["Vocals", "Guitar", "Drums", "Bass"]

    @pytest.mark.skip
    def test_ten(self):
        garden = ["Tulips", "Tomatoes", "Basil", "Peppers"]
        # Call a method to remove and return the first element from the garden array
        first_element = None
        assert garden == ["Tomatoes", "Basil", "Peppers"]
        assert first_element == "Tulips"

    @pytest.mark.skip
    def test_eleven(self):
        teams = ["Rockies", "Avalanche", "Nuggets", "Broncos", "Rapids"]
        # Call a method on the teams variable to get the second, third, and fourth teams
        some_teams = teams
        assert some_teams == ["Avalanche", "Nuggets", "Broncos"]

        # Now use a different method on the teams variable to get the first and second teams
        some_teams = teams
        assert some_teams == ["Rockies", "Avalanche"]

    @pytest.mark.skip
    def test_twelve(self):
        children = ["Sarah", "Owen", "Peter"]
        # Call a method on the children variable to combine them into
        # one string like this: "Sarah, Owen, Peter"
        one_string = None
        assert one_string == "Sarah, Owen, Peter"

    @pytest.mark.skip
    def test_thirteen(self):
        ascending = [1,2,3,4,5]
        # Call a method on the ascending variable to create an array
        # with the elements in the opposite order
        descending = ascending
        assert descending == [5,4,3,2,1]
