import unittest
from math_quiz import random_integer_generator, operator_selector, calculator


class TestMathGame(unittest.TestCase):

    def test_random_integer_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator_selector(self):
        # Test if the function calls successfully generate +, -, or * operator string
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
            operator = operator_selector()
            self.assertIn(operator, valid_operators)


    def test_calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 6, '-', '3 - 6', -3),
                (5, 8, '*', '5 * 8', 40),
                (0, 10, '+', '0 + 10', 10)

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # tests if calculator works
                problem, answer = calculator(num1, num2, operator)
                self.assertEqual(expected_problem, problem)
                self.assertEqual(expected_answer, answer)

if __name__ == "__main__":
    unittest.main()
