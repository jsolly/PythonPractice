import unittest
from GitHub.PythonPractice import code_wars_solutions


class TestClass(unittest.TestCase):
    def test_comp(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [
            11 * 11,
            121 * 121,
            144 * 144,
            19 * 19,
            161 * 161,
            19 * 19,
            144 * 144,
            19 * 19,
        ]
        self.assertTrue(code_wars_solutions.comp(a1, a2))

        a1 = [2, 2, 3]
        a2 = [4, 9, 9]
        self.assertFalse(code_wars_solutions.comp(a1, a2))

        a1 = []
        a2 = []
        self.assertFalse(code_wars_solutions.comp(a1, a2))

        a1 = [0]
        a2 = [0]
        self.assertTrue(code_wars_solutions.comp(a1, a2))

    def test_decode_morse(self):
        code = ".... . -.--   .--- ..- -.. ."
        decoded = code_wars_solutions.decode_morse(code)
        self.assertEqual(decoded, "HEY JUDE")

    def test_find_outlier(self):
        self.assertEqual(code_wars_solutions.find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(
            code_wars_solutions.find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11
        )
        self.assertEqual(
            code_wars_solutions.find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160
        )

        self.assertEqual(
            code_wars_solutions.find_outlier(
                [
                    -4909475,
                    7195239,
                    6063525,
                    -9012935,
                    -6776165,
                    2381193,
                    7217527,
                    1676863,
                    4084677,
                    400289,
                    -2635775,
                    -5608435,
                    4701513,
                    731861,
                    196403,
                    -3692573,
                    5987535,
                    3131225,
                    1999352,
                    -6749383,
                    -9692083,
                    -6912431,
                    -9658485,
                    -7165165,
                    -7036133,
                    -7233649,
                    -4835191,
                    9412189,
                    6791181,
                    -5193163,
                    4406009,
                    -926235,
                    1624687,
                    -5588751,
                    -4692833,
                    3917503,
                ]
            ),
            1999352,
        )

    def test_song_decoder(self):
        self.assertEqual(
            code_wars_solutions.song_decoder(
                "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
            ),
            "WE ARE THE CHAMPIONS MY FRIEND",
        )

        self.assertEqual(
            code_wars_solutions.song_decoder("AWUBBWUBC"),
            "A B C",
            "WUB should be replaced by 1 space",
        )
        self.assertEqual(
            code_wars_solutions.song_decoder("AWUBWUBWUBBWUBWUBWUBC"),
            "A B C",
            "multiples WUB should be replaced by only 1 space",
        )
        self.assertEqual(
            code_wars_solutions.song_decoder("WUBAWUBBWUBCWUB"),
            "A B C",
            "heading or trailing spaces should be removed",
        )

    def test_digital_root_sum(self):  # Digital Root Sum
        self.assertEqual(code_wars_solutions.digital_root_sum(7), 7)
        self.assertEqual(code_wars_solutions.digital_root_sum(16), 7)
        self.assertEqual(code_wars_solutions.digital_root_sum(456), 6)

    def test_fizz_buzz(self):
        fizzbuzz = 15
        fizz = 3
        buzz = 5

        for i in range(30):
            print(code_wars_solutions.fizz_buzz(i))
        self.assertEqual(code_wars_solutions.fizz_buzz(fizzbuzz), "FizzBuzz")
        self.assertEqual(code_wars_solutions.fizz_buzz(fizz), "Fizz")
        self.assertEqual(code_wars_solutions.fizz_buzz(buzz), "Buzz")

    def test_fibonacci_generator(self):
        fib_gen = code_wars_solutions.fibonacci_generator(10)
        first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for fib, num in zip(fib_gen, first_ten):
            self.assertEqual(fib, num)
