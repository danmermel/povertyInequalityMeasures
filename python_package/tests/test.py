import unittest
import pandas as pd

from povertyInequalityMeasures import poverty


class TestPovertyMeasures(unittest.TestCase):
    def test_headline_poverty(self):
        """
        Test the headline poverty function
        """
        data = pd.DataFrame({'total_expenditure': [ 110,120,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_headcount_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.5)

if __name__ == '__main__':
    unittest.main()