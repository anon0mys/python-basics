import pytest


class NestedCollectionsTest:
    def test_one(self):
        coordinates = [[2, 5], [87, 2], [56, 39], [3, 46]]
        # Using the coordinates variable defined above
        # Retrieve the second element
        second = None

        assert second == [87, 2]

    @pytest.mark.skip
    def test_two(self):
        coordinates = [[2, 5], [87, 2], [56, 39], [3, 46]]
        # Using the coordinates variable defined above
        # Retrieve the value 39
        thirty_nine = None
        assert thirty_nine == 39

    @pytest.mark.skip
    def test_three(self):
        coordinates = [[2, 5], [87, 2], [56, 39], [3, 46]]
        # Using the coordinates variable defined above
        # set the last coordinates to [6, 55]

        expected = [[2, 5], [87, 2], [56, 39], [6, 55]]
        assert coordinates == expected

    @pytest.mark.skip
    def test_four(self):
        coordinates = [[2, 5], [87, 2], [56, 39], [3, 46]]
        # Using the coordinates variable defined above
        # set the second element of the last coordinates
        # to 0

        expected = [[2, 5], [87, 2], [56, 39], [3, 0]]
        assert coordinates == expected

    @pytest.mark.skip
    def test_five(self):
        coordinates = [[2, 5], [87, 2], [56, 39], [3, 46]]
        # Using the coordinates variable defined above
        # add the coordinate [4, 14]

        expected = [[2, 5], [87, 2], [56, 39], [3, 46], [4, 14]]
        assert coordinates == expected

    @pytest.mark.skip
    def test_six(self):
        team = {
          "pitchers": ["Kenny", "Joan", "Shabaz"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"]
        }
        # Using the team variable defined above
        # retrieve all of the pitchers
        pitchers = None
        expected = ["Kenny", "Joan", "Shabaz"]
        assert pitchers == expected

    @pytest.mark.skip
    def test_seven(self):
        team = {
          "pitchers": ["Kenny", "Joan", "Shabaz"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"]
        }
        # Using the team variable defined above
        # add "Phil" as a pitcher

        expected = {
          "pitchers": ["Kenny", "Joan", "Shabaz", "Phil"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"]
        }
        assert team == expected

    @pytest.mark.skip
    def test_eight(self):
        team = {
          "pitchers": ["Kenny", "Joan", "Shabaz"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"]
        }
        # Using the team variable defined above
        # create a new key "coaches" with the value
        # of an empty array

        expected = {
          "pitchers": ["Kenny", "Joan", "Shabaz"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"],
          "coaches": []
        }
        assert team == expected

    @pytest.mark.skip
    def test_nine(self):
        team = {
          "pitchers": ["Kenny", "Joan", "Shabaz"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"]
        }
        # Using the team variable defined above
        # Find out how many fielders there are
        num_fielders = None
        assert num_fielders == 5

    @pytest.mark.skip
    def test_ten(self):
        team = {
          "pitchers": ["Kenny", "Joan", "Shabaz"],
          "fielders": ["Luke", "Chris", "Megan", "Mark", "Mackenzie"],
          "catchers": ["Johnny"]
        }
        # Using the team variable defined above
        # Find out if "Kenny" is a pitcher
        kenny_is_pitcher = None
        assert kenny_is_pitcher == True

    @pytest.mark.skip
    def test_eleven(self):
        # HINT: You may find it valuable to break the three_day_forecast variable
        # into multiple lines to make it more readable

        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = 3456789765456787656
        assert actual == expected

    @pytest.mark.skip
    def test_twelve(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}]
        assert actual == expected

    @pytest.mark.skip
    def test_thirteen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = "6-21-18"
        assert actual == expected

    @pytest.mark.skip
    def test_fourteen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = ["days", "date", "ref_num"]
        assert actual == expected

    @pytest.mark.skip
    def test_fifteen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = 55
        assert actual == expected

    @pytest.mark.skip
    def test_sixteen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = ["high", "low", "summary"]
        assert actual == expected

    @pytest.mark.skip
    def test_seventeen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = [77, 64, "Sunny"]
        assert actual == expected

    @pytest.mark.skip
    def test_eighteen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # retrieve the expected piece of information

        actual = None
        expected = "date"
        assert actual == expected

    @pytest.mark.skip
    def test_nineteen(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # Change the high on the fist day to 99

        expected = {"days": [{"high": 99,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        assert three_day_forecast == expected

    @pytest.mark.skip
    def test_20(self):
        three_day_forecast = {"days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        # Using the three_day_forecast variable defined above,
        # Add a new key "time" with the value "12:30"

        expected = {"time": "12:30", "days": [{"high": 70,"low": 63,"summary": "Mostly Sunny"},{"high": 55,"low": 47,"summary": "Partly Cloudy"},{"high": 77,"low": 64,"summary": "Sunny"}], "date": "6-21-18","ref_num": 3456789765456787656}
        assert three_day_forecast == expected
