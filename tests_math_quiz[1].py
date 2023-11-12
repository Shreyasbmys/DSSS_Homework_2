import unittest
from math_quiz_Ex2 import function_ops, function_ops, function_equations


class TestMathGame(unittest.TestCase):

    def test_function_randomVal(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = function_ops(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_ops(self):
        # TODO
        listOps=['+' , '-' , '*' , '/' , '%']
        for i in listOps:
            available_ops = function_ops(random.choice(['+', '-', '*']))
            self.assertTrue(i==available_ops)
        pass

    def test_function_equations(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 5, '-', '6 - 5', 1),
                (8, 4, '*', '8 * 4', 32),
                (7, 6, '+', '7 + 6', 13)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                check_vals = function_equations(num1, num2, operator)
                self.assertTrue(expected_answer == ANSWER )
                pass

if __name__ == "__main__":
    unittest.main()
