from unittest import TestCase

import src.utils.utils as utils


class TestUtils(TestCase):
    def test_simulate_chance(self):
        rates_to_test = [5, 15, 25, 50, 75, 95]
        for test_rate in rates_to_test:
            effective_rate = self._get_effective_rate(test_rate)
            difference = abs(float(test_rate) - effective_rate)
            self.assertTrue(difference < 0.5)

    def test_no_chance(self):
        rates_to_test = [0, 100]
        for test_rate in rates_to_test:
            effective_rate = self._get_effective_rate(test_rate)
            self.assertAlmostEqual(test_rate, effective_rate)

    def test_join_multi_line_strings(self):
        string_a = "A1     \nA2     \nA3     "
        string_b = "B1     \nB2     "
        string_c = "C1     \nC2     \nC3  "
        expected_string = "A1     B1     C1     \nA2     B2     C2     \nA3            C3  \n"
        blocks = [string_a, string_b, string_c]
        actual_string = utils.join_multi_line_strings(blocks, 7)
        self.assertEqual(expected_string, actual_string)

        string_a = "A1     \nA2     \nA3     "
        string_b = "B1     \nB2     \nB3     \nB4     "
        string_c = "C1     \nC2     \nC3  "
        expected_string = "A1     B1     C1     \nA2     B2     C2     \nA3     B3     C3  \n       B4            \n"
        blocks = [string_a, string_b, string_c]
        actual_string = utils.join_multi_line_strings(blocks, 7)
        self.assertEqual(expected_string, actual_string)

    def _get_effective_rate(self, test_rate):
        num_success = 0
        num_tests = 100000
        for _ in xrange(num_tests):
            if utils.simulate_chance(test_rate):
                num_success += 1
        return float(num_success) * 100 / num_tests