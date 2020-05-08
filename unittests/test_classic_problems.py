try:
    import unittest
    import classic_problems
except Exception as e:
    print(f"Some modules are missing!{e}")

classic_problems.fizz_buzz(5)

class TestClass(unittest.TestCase):
    def test_fizz_buzz(self):
        fizzbuzz = 15
        fizz = 3
        buzz = 5

        self.assertEqual(classic_problems.fizz_buzz(fizzbuzz), "fizzbuzz")
        self.assertEqual(classic_problems.fizz_buzz(fizz), "fizz")
        self.assertEqual(classic_problems.fizz_buzz(buzz), "fizzbuzz")