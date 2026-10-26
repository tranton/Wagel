# test_salary_calculator.py

import unittest
from salary_calculator import calculate_net_salary

class TestSalaryCalculator(unittest.TestCase):

    def test_calculate_net_salary_region1_no_dependents(self):
        # Test case for Region 1 with no dependents
        gross_salary = 50000000
        region = 1
        num_dependents = 0

        net_salary, tax, social, health, unemployment = calculate_net_salary(gross_salary, region, num_dependents)

        # Corrected expected values based on manual calculation
        self.assertAlmostEqual(net_salary, 41001750.0, places=2)
        self.assertAlmostEqual(tax, 5667250.0, places=2)
        self.assertAlmostEqual(social, 2384000.0, places=2)
        self.assertAlmostEqual(health, 447000.0, places=2)
        self.assertAlmostEqual(unemployment, 500000.0, places=2)

    def test_calculate_net_salary_region2_with_dependents(self):
        # Test case for Region 2 with 2 dependents
        gross_salary = 60000000
        region = 2
        num_dependents = 2

        net_salary, tax, social, health, unemployment = calculate_net_salary(gross_salary, region, num_dependents)

        # Corrected expected values based on manual calculation
        self.assertAlmostEqual(net_salary, 50626750.0, places=2)
        self.assertAlmostEqual(tax, 5942250.0, places=2)
        self.assertAlmostEqual(social, 2384000.0, places=2)
        self.assertAlmostEqual(health, 447000.0, places=2)
        self.assertAlmostEqual(unemployment, 600000.0, places=2)

    def test_calculate_net_salary_invalid_input(self):
        # Test case with invalid (non-numeric) input
        gross_salary = "abc"
        region = 1
        num_dependents = 0

        result = calculate_net_salary(gross_salary, region, num_dependents)

        self.assertEqual(result, (None, None, None, None, None))

if __name__ == '__main__':
    unittest.main()
