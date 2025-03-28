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

    def test_poverty_gap(self):
        """
        Test the poverty gap index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_poverty_gap_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.08)
    
    def test_poverty_severity(self):
        """
        Test the poverty severity index function
        """
        data = pd.DataFrame({'total_expenditure': [ 100,110,150,160], 'weight':[1,1,1,1]})
        poverty_line= 125
        result = poverty.get_poverty_severity_index(poverty_line, data, "total_expenditure","weight")
        self.assertEqual(result, 0.0136)


if __name__ == '__main__':
    unittest.main()