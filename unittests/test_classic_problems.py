import unittest
from GitHub.PythonPractice import classic_problems


class TestClass(unittest.TestCase):
    def test_fizz_buzz(self):
        fizzbuzz = 15
        fizz = 3
        buzz = 5

        for i in range(30):
            print(classic_problems.fizz_buzz(i))
        self.assertEqual(classic_problems.fizz_buzz(fizzbuzz), "FizzBuzz")
        self.assertEqual(classic_problems.fizz_buzz(fizz), "Fizz")
        self.assertEqual(classic_problems.fizz_buzz(buzz), "Buzz")

    def test_fibonacci_generator(self):
        fib_gen = classic_problems.fibonacci_generator(10)
        first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for fib, num in zip(fib_gen, first_ten):
            self.assertEqual(fib, num)
