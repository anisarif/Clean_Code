import unittest

from disabilityAmount_improvements import disabilityAmount

class TestCalculateDisabilityBenefit(unittest.TestCase):

    def test_eligible_for_benefit(self):
        result = disabilityAmount(2, 6, False, 65, 70, 30000, "disability")
        self.assertEqual(result, 21000.0)

    def test_not_eligible_for_benefit(self):
        result = disabilityAmount(1, 6, False, 60, 50, 50000, "disability")
        self.assertEqual(result, 0)

    def test_age_below_minimum(self):
        result = disabilityAmount(3, 6, False, 61, 70, 30000, "health")
        self.assertEqual(result, 0)

    def test_months_disabled_exceeds_limit(self):
        result = disabilityAmount(3, 13, False, 65, 70, 30000, "disability")
        self.assertEqual(result, 0)

    def test_is_part_time(self):
        result = disabilityAmount(4, 6, True, 70, 70, 30000, "disability")
        self.assertEqual(result, 0)

    def test_disability_percentage_below_minimum(self):
        result = disabilityAmount(5, 6, False, 70, 59, 30000, "disability")
        self.assertEqual(result, 0)

    def test_income_above_limit(self):
        result = disabilityAmount(6, 6, False, 70, 70, 45000, "disability")
        self.assertEqual(result, 0)

    def test_different_insurance_type(self):
        result = disabilityAmount(7, 6, False, 70, 70, 30000, "health")
        self.assertEqual(result, 0)



if __name__ == "__main__":
    unittest.main()