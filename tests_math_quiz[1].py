import unittest
from math_quiz import number_limit, function_ops, function_equations


class TestMathGame(unittest.TestCase):

    def test_function_randomVal(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = number_limit(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_operation(self):
        # TODO
        listOps=['+' , '-' , '*' , '/' , '%']
        for i in listOps:
            available_ops = function_ops(random.choice(['+', '-', '*']))
            self.assertTrue(i==available_ops)
        pass

    def test_function_Calculation(self):
        test_cases = [
    (3, 2, '+', '3 + 2', 5),
    (5, 5, '-', '5 - 5', 0),
    (8, 5, '*', '8 * 5', 40),
    (6, 6, '+', '6 + 6', 12)
                     ]

       for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
           calculated_problem, calculated_answer = function_equations(num_1, num_2, operator)
           self.assertTrue (calculated_problem == expected_problem)
           self.assertTrue (calculated_answer == expected_answer)
           print(f"Test Passed: {calculated_problem} = {calculated_answer}")


if name == "main":
   unittest.main()
