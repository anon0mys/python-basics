import pytest


class InjectPatternTest:
    def test_1(self):

        numbers = [28, 12, 38, 1, 91]
        # Iterate over the numbers array defined above,
        # to find the difference of all the numbers
        difference = 0
        for number in numbers:
            difference = difference - number

        assert difference == -170

    def test_2(self):
        bills = {
            "rent": 800,
            "car": 240,
            "insurance": 110,
            "medical": 1112
        }
        # Iterate over the bills hash defined above
        # to find the difference of all the values

        difference = 0
        for bill in bills:
            difference -= bills[bill]

        assert difference == -2262

    @pytest.mark.skip
    def test_3(self):
        numbers = [2, 3, 5, 7]
        # Iterate over the numbers array defined above
        # to find the product of all the numbers

        product = 1
        # Your Code Here

        assert product == 210

    @pytest.mark.skip
    def test_4(self):
        scrabble_score = {
            "letter_total": 23,
            "word_muliplier": 3,
            "bonus": 2
        }
    # Iterate over the scarbble_score hash defined above
        # to find the product of all the values

        product = 1
        # Your Code Here

        assert product == 138

    @pytest.mark.skip
    def test_5(self):
        airlines = ["Southwest", "Delta", "United", "Frontier"]
        # Iterate over the airlines array defined above to
        # create a hash with the name of the airline as the
        # key and the length of the name as the value

        number_of_letters = {}
        # Your Code Here

        expected = {
            "Southwest": 9,
            "Delta": 5,
            "United": 6,
            "Frontier": 8
        }
        assert number_of_letters == expected

    @pytest.mark.skip
    def test_6(self):
        topping_calories = {
            "pepperoni": 430,
            "sausage": 400,
            "olives": 10,
            "peppers": 10,
            "onions": 20
        }
        # Iterate over the topping_calories hash defined above
        # to create an array of all the toppings

        toppings = []
        # Your Code Here

        assert toppings == ["pepperoni", "sausage", "olives", "peppers", "onions"]

    @pytest.mark.skip
    def test_7(self):
        elements = [["a", 1], ["b", 9], ["c", 21]]
        # Iterate over the elements array defined above
        # to find the sum of all the integers

        # Your Code Here
        sum_of_second_values = None

        assert sum_of_second_values == 31

    @pytest.mark.skip
    def test_8(self):
        toppings = {
            "pepperoni": {
                "calories": 430,
                "quantity": 5
            },
            "sausage": {
                "calories": 400,
                "quantity": 10
            },
            "olives": {
                "calories": 10,
                "quantity": 20
            },
            "peppers": {
                "calories": 10,
                "quantity": 20
            },
            "onions": {
                "calories": 20,
                "quantity": 20
            }
        }
        # Iterate over the toppings array defined above to find
        # total calories. You will need to multiply each topping's
        # calorie count by the quantity

        # Your Code Here
        total_calories = None

        assert total_calories == 6950

    @pytest.mark.skip
    def test_9(self):
        grades = {
            "quizzes": [8, 5, 3, 6, 5],
            "tests": [23, 21, 24],
            "essays": [10, 11, 10],
            "final": [47]
        }
        # Iterate over the elements array defined above
        # to calculate the final grade. The final grade is
        # calculated by averaging each category together and
        # summing all of the averages

        # Your code goes here
        final_grade = None

        assert final_grade == 85.40

    @pytest.mark.skip
    def test_10(self):
        menu = {
            "empanadas": {
                "flavors": ["chicken", "potato", "steak", "veggie"],
                "gluten_free": False
            },
            "scones": {
                "flavors": ["blueberry", "vanilla"],
                "gluten_free": False
            },
            "parfaits": {
                "flavors": ["blueberry", "strawberry", "cherry"],
                "gluten_free": True
            }
        }

        # Iterate over the menu hash above to create a printable
        # version of the menu

        # Your Code Here
        printable_menu = None

        expected = "Menu:\n" \
                   "- chicken, potato, steak, and veggie empanadas (non gluten free)\n" \
                   "- blueberry, and vanilla scones (non gluten free)\n" \
                   "- blueberry, strawberry, and cherry parfaits (gluten free)\n"

        assert printable_menu == expected
