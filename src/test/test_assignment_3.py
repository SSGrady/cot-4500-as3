import unittest
from src.main.assignment_3 import euler_method, runge_kutta_method

class TestAssignment3(unittest.TestCase):

    def test_euler_method(self):
        func = lambda t, y: t - y**2
        t_range = (0, 2)
        initial_val = 1
        iterations = 10
        expected_result = 1.2446380979332121
        result = euler_method(func, t_range, initial_val, iterations)
        self.assertAlmostEqual(result, expected_result, places=10)

    def test_runge_kutta_method(self):
        func = lambda t, y: t - y**2
        t_range = (0, 2)
        initial_val = 1
        iterations = 10
        expected_result = 1.251316587879806
        result = runge_kutta_method(func, t_range, initial_val, iterations)
        self.assertAlmostEqual(result, expected_result, places=10)

if __name__ == '__main__':
    unittest.main()