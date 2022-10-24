import pytest


class StringsTest:
    def test_one(self):
        name = "alice"

        # In place of the line below, use a standard function to capitalize name
        # actual = <your code here>
        actual = name.capitalize()


        expected = "Alice"

        assert actual == expected


    def test_two(self):
        name = "aLiCe"
        # In place of the line below, call a method to achieve the expected output.
        actual = name.upper()
        expected = "ALICE"

        assert actual == expected


    def test_three(self):
        name = "AlIcE"
        # In place of the line below, call a method to achieve the expected output.
        actual = name.lower()
        expected = "alice"

        assert actual == expected


    def test_four(self):
        rhyme = "peter piper picked a peck of picked peppers"
        # In place of the line below, call a method to achieve the expected output.
        actual = rhyme[::-1]
        expected = "sreppep dekcip fo kcep a dekcip repip retep"

        assert actual == expected


    def test_five(self):
        word = "ticking"
        # In place of the line below, call a method to achieve the expected output.
        actual = word.replace("t", "k")
        expected = "kicking"

        assert actual == expected


    def test_six(self):
        word = "ticking"
        # In place of the line below, call a method to achieve the expected output.
        actual = word.replace("ticking", "clocking")
        expected = "clocking"

        assert actual == expected


    def test_seven(self):
        words = "five sleepy kittens"
        # In place of the line below, call a method to achieve the expected output.
        actual = words.replace("e", "*")
        expected = "fiv* sl**py kitt*ns"

        assert actual == expected


    def test_eight(self):
        greeting = "Hello!!"
        # In place of the line below, call a method to achieve the expected output.
        actual = greeting[:-1]
        expected = "Hello!"

        assert actual == expected


    def test_nine(self):
        greeting = "Hello!!\n"
        # In place of the line below, call a method to achieve the expected output.
        actual = greeting[:-1]
        expected = "Hello!!"

        assert actual == expected


    def test_ten(self):
        greeting = "Hello!!\n\n"
        # In place of the line below, call a method to achieve the expected output.
        actual = greeting[:-1]
        expected = "Hello!!\n"

        assert actual == expected


    def test_eleven(self):
        rhyme = "eeny, meeny, miny, moe"
        # In place of the line below, call a method to achieve the expected output.
        actual = rhyme.replace("e", "")
        expected = "ny, mny, miny, mo"

        assert actual == expected

    def test_twelve(self):
        rhyme = "eeny, meeny, miny, moe"
        # In place of the line below, call a method to achieve the expected output.
        actual =
        expected = "ny, mny, mny, m"

        assert actual == expected

    @pytest.mark.skip
    def test_thirteen(self):
        greeting = "Hello World!"
        # In place of the line below, call a method to get the number of characters in the string
        actual = None
        expected = 12

        assert actual == expected

    @pytest.mark.skip
    def test_fourteen(self):
        greeting = "Hello World!\n"
        # In place of the line below, call a method to get the number of characters in the string
        actual = None
        expected = 13

        assert actual == expected

    @pytest.mark.skip
    def test_fifteen(self):
        greeting = "Hello       World!"
        # In place of the line below, call a method to get the number of characters in the string
        actual = None
        expected = 18

        assert actual == expected

    @pytest.mark.skip
    def test_sixteen(self):
        greeting = "Hello World!"
        # In place of the line below, call a method to get the number of 'o' in the string
        actual = None
        expected = 2

        assert actual == expected

    @pytest.mark.skip
    def test_seventeen(self):
        greeting = "Hello World!"
        # In place of the line below, call a method to get the number of vowels in the string
        actual = None
        expected = 3

        assert actual == expected

    @pytest.mark.skip
    def test_eighteen(self):
        greeting = "Hello World!"
        # In place of the line below, call a method to check if the string includes 'llo'
        actual = None
        expected = True

        assert actual == expected

    @pytest.mark.skip
    def test_nineteen(self):
        greeting = "Hello World!"
        # In place of the line below, call a method to check if the string includes 'lol'
        actual = None
        expected = False

        assert actual == expected

    @pytest.mark.skip
    def test_twenty(self):
        greeting = "Hello World, my name is"
        name = "Harry Potter"
        # In place of the line below, use string manipulation to combine the
        # greeting and name variables to achieve the expected outcome
        actual = None
        expected = "Hello World, my name is Harry Potter"

        assert actual == expected

    @pytest.mark.skip
    def test_twenty_one(self):
        greeting = "Hello World, my name is"
        name = "Harry Potter"
        # See if you can use another method than the last test to achieve the same goal:
        actual = None
        expected = "Hello World, my name is Harry Potter"

        assert actual == expected

    @pytest.mark.skip
    def test_twenty_two(self):
        phrase = "  \n\t to the moon\n\n\t    "
        # In place of the line below, call a method to achieve the expected outcome
        actual = None
        expected = "to the moon"

        assert actual == expected
